from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId


user = APIRouter()


@user.get('/')
async def find_all_users():
    return usersEntity(conn.MarttechDB.user.find())


@user.get('/{id}')
async def find_one_user(id):
    return userEntity(conn.MarttechDB.user.find_one({"_id": ObjectId(id)}))


@user.post('/')
async def create_user(user: User):
    conn.MarttechDB.user.insert_one(dict(user))
    return usersEntity(conn.MarttechDB.user.find())


@user.patch('/{id}')
async def update_user(id, user: User):
    conn.MarttechDB.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return userEntity(conn.MarttechDB.user.find_one({"_id": ObjectId(id)}))


@user.delete('/{id}')
async def delete_user(id):
    return userEntity(conn.MarttechDB.user.find_one_and_delete({"_id": ObjectId(id)}))

