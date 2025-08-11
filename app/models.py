from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True, nullable=False)
    descricao = Column(String, nullable=True)
    concluido = Column(Boolean, default=False)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())