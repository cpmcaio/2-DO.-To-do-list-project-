from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluido: bool = False

class TarefaCreate(TarefaBase):
    pass

class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    concluido: Optional[bool] = None

class Tarefa(TarefaBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True