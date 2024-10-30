# Robometrics

## Sobre o Projeto
Robometrics é um sistema desenvolvido em Django para a equipe de robótica da faculdade. Este projeto foi criado para facilitar o acompanhamento de métricas de desempenho e dados das competições da equipe, permitindo que membros da equipe e supervisores acompanhem o progresso de seus robôs e realizem análises de desempenho.

O objetivo do Robometrics é fornecer uma plataforma intuitiva e confiável para monitorar o desempenho dos robôs em diferentes atividades, além de armazenar dados históricos para consulta futura e otimização dos robôs.

## Funcionalidades
- Armazenamento de histórico de desempenho, permitindo análises a longo prazo.
- Interface intuitiva para que os membros da equipe possam visualizar dados e métricas facilmente.
- Relatórios customizáveis para suporte em análises e planejamentos futuros da equipe.

## Pré-requisitos
Antes de começar, certifique-se de ter instalado:

- Python 3
- pip (gerenciador de pacotes Python)
- virtualenv (opcional, mas recomendado para isolar as dependências do projeto)

## Instalação e Configuração

1. Clone o repositório:
    bash
    git clone https://github.com/seu-usuario/robometrics.git
    

2. Navegue até o diretório do projeto:
    bash
    cd robometrics
    

3. Crie um ambiente virtual (opcional, mas recomendado):
    bash
    python3 -m venv .venv
    

4. Ative o ambiente virtual:
    bash
    source .venv/bin/activate
    

5. Instale as dependências do projeto:
    bash
    pip install -r requirements.txt
    

6. Execute as migrações do banco de dados:
    bash
    python manage.py migrate
    

7. Inicie o servidor de desenvolvimento:
    bash
    python manage.py runserver
    

8. Acesse a aplicação em seu navegador web:
    
    http://127.0.0.1:8000/
