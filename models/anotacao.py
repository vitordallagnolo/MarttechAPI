from beanie import Document, Link
from datetime import date
from models.tag import Tag
from models.caderno import Caderno


class Anotacao(Document):
    titulo: str
    data_criacao: date
    data_modificacao: date
    texto: str
    tags: Tag
    caderno: Link[Caderno]


