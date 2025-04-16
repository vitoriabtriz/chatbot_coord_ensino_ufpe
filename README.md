# Chatbot para Coordenação de Ensino - Centro de Informática da UFPE

Este projeto é um chatbot desenvolvido para a Coordenação de Ensino do Centro de Informática da UFPE, com o objetivo de auxiliar alunos, professores e demais membros da comunidade acadêmica a obter informações rápidas sobre processos administrativos, datas importantes e outros serviços relacionados ao curso e à instituição.

## Funcionalidades

- **Atendimento ao aluno**: O chatbot pode responder a perguntas frequentes sobre a coordenação de ensino, como informações sobre matrícula, prazos, documentos necessários, etc.
- **Consultas a dados**: O chatbot tem a capacidade de acessar e fornecer informações sobre eventos, disciplinas e processos acadêmicos.
- **Interação personalizada**: Ele pode fornecer respostas de acordo com o perfil do usuário, com base em informações pré-definidas.

## Como Usar

### 1. Pré-requisitos

Certifique-se de que você tem o seguinte instalado:

- **Python 3.6 ou superior**
- **Bibliotecas necessárias**: As dependências estão listadas no arquivo `requirements.txt`. Para instalar as bibliotecas, execute o seguinte comando:

  ```bash
  pip install -r requirements.txt
  ```

### 2. Configuração do Ambiente

- **Criando um ambiente virtual (recomendado)**:
  
  Para isolar as dependências do projeto, recomendamos a criação de um ambiente virtual:

  - **Para Linux/macOS**:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

  - **Para Windows**:

    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```

- **Instalar dependências**:
  
  Depois de ativar o ambiente virtual, instale as dependências com:

  ```bash
  pip install -r requirements.txt
  ```

### 3. Executando o Projeto

- Após a configuração, para iniciar o chatbot, basta rodar o seguinte comando no terminal:

  ```bash
  python main.py
  ```

  Isso inicializará o servidor do chatbot e o tornará acessível localmente no seguinte endereço:

  [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 4. Interagindo com o Chatbot

1. **Acessando o chatbot**: Após iniciar o servidor, abra o navegador e acesse a URL fornecida.
2. **Conversa**: Inicie uma conversa com o chatbot. Você pode fazer perguntas relacionadas à coordenação de ensino, como:
   - Quais são os prazos de matrícula?
   - Como posso fazer uma migração de curso?
   - Como posso migrar de perfil curricular?
3. **Respostas**: O chatbot fornecerá respostas baseadas nas informações configuradas, como datas de eventos, informações sobre documentos, entre outros.

### 5. Arquivos de Configuração

- O chatbot foi configurado para responder a uma série de perguntas e fornecer informações sobre a coordenação de ensino. As respostas podem ser ajustadas diretamente no código ou configuradas de acordo com as necessidades da Coordenação.

### 6. Arquivos Ignorados

- Arquivos sensíveis ou temporários, como arquivos de ambiente (`.env`) e diretórios de ambiente virtual (`env/`), estão ignorados no repositório com o uso de um arquivo `.gitignore`.

