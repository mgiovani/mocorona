from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/resumos/", response_model=schemas.Resumo)
def create_resumo(resumo: schemas.ResumoCreate, db: Session = Depends(get_db)):
    db_resumo = crud.get_resumo_by_data(db, data_atualizacao=resumo.data_atualizacao)
    if db_resumo:
        raise HTTPException(status_code=400, detail="Resumo para esta data já foi cadastrado")
    return crud.create_resumo(db=db, resumo=resumo)


@app.get("/resumos/", response_model=List[schemas.Resumo])
def read_resumos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resumos = crud.get_resumos(db, skip=skip, limit=limit)
    return resumos


@app.get("/resumos/{resumo_id}", response_model=schemas.Resumo)
def read_resumo(resumo_id: int, db: Session = Depends(get_db)):
    db_resumo = crud.get_resumo(db, resumo_id=resumo_id)
    if db_resumo is None:
        raise HTTPException(status_code=404, detail="Resumo não encontrado")
    return db_resumo
