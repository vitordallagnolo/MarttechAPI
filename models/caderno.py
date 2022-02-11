from typing import List
from pydantic import BaseModel


class Caderno(BaseModel):
    descricao: str
    anotacoes: List[str] = []

