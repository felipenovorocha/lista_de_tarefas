from models.categoria import Categoria 
from pydantic import BaseModel

class Tarefa(BaseModel):
    id:int
    nome:str
    favorito:bool
    categoria:Categoria
