from sqlalchemy.orm import Session
from . import models, schemas

def get_tarefas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tarefa).offset(skip).limit(limit).all()

def get_tarefa(db: Session, tarefa_id: int):
    return db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()

def create_tarefa(db: Session, tarefa: schemas.TarefaCreate):
    db_tarefa = models.Tarefa(**tarefa.dict())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

def update_tarefa(db: Session, tarefa_id: int, tarefa: schemas.TarefaUpdate):
    db_tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if db_tarefa:
        for key, value in tarefa.dict(exclude_unset=True).items():
            setattr(db_tarefa, key, value)
        db.commit()
        db.refresh(db_tarefa)
    return db_tarefa

def delete_tarefa(db: Session, tarefa_id: int):
    db_tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if db_tarefa:
        db.delete(db_tarefa)
        db.commit()
    return db_tarefa