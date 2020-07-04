from datetime import date

from sqlalchemy.orm import Session

import models, schemas


def get_resumo(db: Session, resumo_id: int):
    return db.query(models.Resumo).filter(models.Resumo.id == resumo_id).first()


def get_resumo_by_data(db: Session, data_atualizacao: date):
    return db.query(models.Resumo).filter(models.Resumo.data_atualizacao == data_atualizacao).first()


def get_resumos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Resumo).offset(skip).limit(limit).all()


def create_resumo(db: Session, resumo: schemas.ResumoCreate):
    db_resumo = models.Resumo(
        notificacoes=resumo.notificacoes,
        negativos=resumo.negativos,
        confirmados=resumo.confirmados,
        recuperados=resumo.recuperados,
        obitos=resumo.obitos,
        data_atualizacao=resumo.data_atualizacao
    )
    db.add(db_resumo)
    db.commit()
    db.refresh(db_resumo)
    return db_resumo