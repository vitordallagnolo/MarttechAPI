from fastapi import FastAPI
from routes.user import user
from routes.anotacao import anotacao
from routes.caderno import caderno
from routes.tag import tag
app = FastAPI()
app.include_router(user)
app.include_router(anotacao)
app.include_router(caderno)
app.include_router(tag)
