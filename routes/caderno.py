from fastapi import APIRouter
from models.caderno import Caderno
from config.db import conn
from schemas.caderno import cadernoEntity, cadernosEntity
from bson import ObjectId


caderno = APIRouter()


@caderno.get('/caderno/')
async def find_all_cadernos():
    print(conn.MarttechDB.caderno.find())
    print(cadernosEntity(conn.MarttechDB.caderno.find()))
    return cadernosEntity(conn.MarttechDB.caderno.find())


@caderno.get('/caderno/{id}')
async def find_one_caderno(id):
    return cadernoEntity(conn.MarttechDB.caderno.find_one({"_id": ObjectId(id)}))


@caderno.post('/caderno/')
async def create_caderno(caderno: Caderno):
    conn.MarttechDB.caderno.insert_one(dict(caderno))
    return cadernosEntity(conn.MarttechDB.caderno.find())


@caderno.patch('/caderno/{id}')
async def update_caderno(id, caderno: Caderno):
    conn.MarttechDB.caderno.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(caderno)
    })
    return cadernoEntity(conn.MarttechDB.caderno.find_one({"_id": ObjectId(id)}))


@caderno.delete('/caderno/{id}')
async def delete_caderno(id):
    return cadernoEntity(conn.MarttechDB.caderno.find_one_and_delete({"_id": ObjectId(id)}))

