from fastapi import APIRouter
from models.anotacao import Anotacao
from config.db import conn
from schemas.anotacao import anotacaoEntity, anotacoesEntity
from bson import ObjectId


anotacao = APIRouter()


@anotacao.get('/caderno/nota/')
async def find_all_notas():
    print(conn.MarttechDB.anotacao.find())
    print(anotacoesEntity(conn.MarttechDB.anotacao.find()))
    return anotacoesEntity(conn.MarttechDB.anotacao.find())


@anotacao.get('/caderno/nota/{id}')
async def find_one_note(id):
    return anotacaoEntity(conn.MarttechDB.anotacao.find_one({"_id": ObjectId(id)}))


@anotacao.post('/caderno/nota/')
async def create_note(anotacao: Anotacao):
    conn.MarttechDB.anotacao.insert_one(dict(anotacao))
    return anotacoesEntity(conn.MarttechDB.anotacao.find())


@anotacao.patch('/caderno/nota/{id}')
async def update_note(id, anotacao: Anotacao):
    conn.MarttechDB.anotacao.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(anotacao)
    })
    return anotacaoEntity(conn.MarttechDB.anotacao.find_one({"_id": ObjectId(id)}))


@anotacao.delete('/caderno/nota/{id}')
async def delete_note(id):
    return anotacaoEntity(conn.MarttechDB.anotacao.find_one_and_delete({"_id": ObjectId(id)}))

