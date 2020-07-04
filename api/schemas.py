from typing import List, Optional

from pydantic import BaseModel


class ResumoBase(BaseModel):
    notificacoes: int
    negativos: int
    confirmados: int
    recuperados: int
    obitos: int
    data_atualizacao: str

class ResumoCreate(ResumoBase):
    pass


class Resumo(ResumoBase):
    id: int

    class Config:
        orm_mode = True