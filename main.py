import os
from openai import OpenAI
import shutil
from tqdm import tqdm
import concurrent.futures
import gradio as gr
from dotenv import load_dotenv

#carrega a chave da OpenAI do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

#caminho onde estarão os PDFs
dir_pdfs = 'input_pdfs'
os.makedirs(dir_pdfs, exist_ok=True)

#lista os arquivos da pasta
pdf_files = [os.path.join(dir_pdfs, f) for f in os.listdir(dir_pdfs) if f.endswith('.pdf')]

#função para criar o vetor
def create_vector_store(store_name: str) -> dict:
    try:
        vector_store = client.vector_stores.create(name=store_name)
        return {
            "id": vector_store.id,
            "name": vector_store.name,
            "created_at": vector_store.created_at,
            "file_count": vector_store.file_counts.completed
        }
    except Exception as e:
        print(f"Erro ao criar o vector store: {e}")
        return {}

#upload de arquivos pdf
def upload_single_pdf(file_path: str, vector_store_id: str):
    file_name = os.path.basename(file_path)
    try:
        file_response = client.files.create(file=open(file_path, 'rb'), purpose="assistants")
        attach_response = client.vector_stores.files.create(
            vector_store_id=vector_store_id,
            file_id=file_response.id
        )
        return {"file": file_name, "status": "success"}
    except Exception as e:
        print(f"Erro com {file_name}: {str(e)}")
        return {"file": file_name, "status": "failed", "error": str(e)}

def upload_pdf_files_to_vector_store(vector_store_id: str, pdf_files: list):
    stats = {"total_files": len(pdf_files), "successful_uploads": 0, "failed_uploads": 0, "errors": []}
    print(f"{len(pdf_files)} PDFs serão processados...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(upload_single_pdf, file_path, vector_store_id): file_path for file_path in pdf_files}
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(pdf_files)):
            result = future.result()
            if result["status"] == "success":
                stats["successful_uploads"] += 1
            else:
                stats["failed_uploads"] += 1
                stats["errors"].append(result)

    return stats

#resposta do bot
def response_output(query, history):
    def make_request():
        return client.responses.create(
            model="gpt-4o-mini",
            input=[
                {
                    "role": "system",
                    "content": "Você é um assistente virtual que responde apenas com base nos documentos fornecidos sobre a coordenação do CIn/UFPE. Caso a pergunta não tenha relação com os dados, responda: 'Desculpe, não sei informar sobre isso.'"
                },
                {"role": "user", "content": query}
            ],
            tools=[{"type": "file_search", "vector_store_ids": [vector_store_details['id']]}]
        )

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(make_request)
            response = future.result(timeout=30)

        if (hasattr(response, "output")
            and len(response.output) > 1
            and hasattr(response.output[1], "content")
            and response.output[1].content
            and response.output[1].content[0].text.strip() != ""):
            return response.output[1].content[0].text.strip()
        else:
            return "Desculpe, não sei informar sobre isso."
    except:
        return "Desculpe, não sei informar sobre isso."

#executar tudo
if __name__ == "__main__":
    store_name = "coordenacao_ensino"
    vector_store_details = create_vector_store(store_name)
    upload_pdf_files_to_vector_store(vector_store_details["id"], pdf_files)

    demo = gr.ChatInterface(response_output, type="messages")
    demo.launch()
