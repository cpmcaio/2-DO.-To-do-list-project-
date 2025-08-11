from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/tarefas",
    tags=["tarefas"],
)

@router.get("/", response_model=List[schemas.Tarefa])
def listar_tarefas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tarefas(db, skip=skip, limit=limit)

@router.get("/{tarefa_id}", response_model=schemas.Tarefa)
def obter_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = crud.get_tarefa(db, tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@router.post("/", response_model=schemas.Tarefa, status_code=201)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    return crud.create_tarefa(db, tarefa)

@router.put("/{tarefa_id}", response_model=schemas.Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa: schemas.TarefaUpdate, db: Session = Depends(get_db)):
    tarefa_atualizada = crud.update_tarefa(db, tarefa_id, tarefa)
    if tarefa_atualizada is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_atualizada

@router.delete("/{tarefa_id}", response_model=schemas.Tarefa)
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa_deletada = crud.delete_tarefa(db, tarefa_id)
    if tarefa_deletada is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_deletada