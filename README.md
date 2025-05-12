# FastApi
Creating REST API in Python


CRIANDO UM AMBIENTE VIRTUAL 
python -m venv venv

ATIVANDO AMBIENTE VIRTUAL

.\venv\Scripts\Activate.ps1

INSTALAÇÃO DE DEPENDÊNCIAS DENTRO DA APLICAÇÃO

pip install fastapi

pip install uvicorn

EXECUTANDO API

uvicorn main:app --reload

Como FastAPI nos fornece documentação interativa com Swagger para acessar usaremos o : http://127.0.0.1:8000/docs

Endpoints Disponíveis 

GET  ->  /tarefas -> Lista todas as tarefas
GET  ->  /tarefas/{id} -> Retorna uma tarefa específica
POST ->  /tarefas -> Cria uma nova tarefa 
PUT  ->  /tarefas/{id} -> Atualiza uma tarefa
DELETE -> /tarefas/{id} -> Remove uma tarefa
