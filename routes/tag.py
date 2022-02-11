from fastapi import APIRouter
from models.tag import Tag
from config.db import conn
from schemas.tag import tagEntity, tagsEntity
from bson import ObjectId


tag = APIRouter()


@tag.get('/tag/')
async def find_all_tags():
    print(conn.MarttechDB.tag.find())
    print(tagsEntity(conn.MarttechDB.tag.find()))
    return tagsEntity(conn.MarttechDB.tag.find())


@tag.get('/tag/{id}')
async def find_one_tag(id):
    return tagEntity(conn.MarttechDB.tag.find_one({"_id": ObjectId(id)}))


@tag.post('/tag/')
async def create_tag(tag: Tag):
    conn.MarttechDB.tag.insert_one(dict(tag))
    return tagsEntity(conn.MarttechDB.tag.find())


@tag.patch('/tag/{id}')
async def update_tag(id, tag: Tag):
    conn.MarttechDB.tag.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(tag)
    })
    return tagEntity(conn.MarttechDB.tag.find_one({"_id": ObjectId(id)}))


@tag.delete('/tag/{id}')
async def delete_tag(id):
    return tagEntity(conn.MarttechDB.tag.find_one_and_delete({"_id": ObjectId(id)}))

