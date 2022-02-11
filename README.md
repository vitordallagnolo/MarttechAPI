# fastapi-beanie-pydantic-pymongo
Exemplo FastAPI server com conexão MongoDB

## Intro

Essa API foi criada para [MongoDB]() com as seguintes features:

- Criação de Usuário
- Criação de Caderno de Anotações
- Criação de Anotações
- Criação de TAGs
- Todos os modelos CRUD

## Setup

Escrito em Python 3.10 and above. Nãs esqueça da virtualenv. Os comandos`python` a baixo serão para instalação e execução.

Primeiro é necessário instalar os requirements.

```bash
python -m pip install -r requirements.txt
```

Antes de rodar a aplicação, é necessário configurar o seu banco de dados no arquivo db.py.


```bash
conn = MongoClient("mongodb+srv://[usuário]:[senha]@[database].bi9kl.mongodb.net/[DataBase]?retryWrites=true&w=majority")

```

## Run

Este modelo usa [uvicorn]() como ASGI web server.

```bash
uvicorn index:app --reload
```

A API estará disponível em http://localhost:8080


[MongoDB]: https://www.mongodb.com "MongoDB NoSQL homepage"
