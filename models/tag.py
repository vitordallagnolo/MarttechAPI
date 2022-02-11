from pydantic import BaseModel


class Tag(BaseModel):
    nome: str
    descricao: str


