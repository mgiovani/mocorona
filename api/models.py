from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database import Base


class Resumo(Base):
    __tablename__ = "resumos"

    id = Column(Integer, primary_key=True, index=True)
    notificacoes =  Column(Integer)
    negativos = Column(Integer)
    confirmados = Column(Integer)
    recuperados = Column(Integer)
    obitos = Column(Integer)
    data_atualizacao = Column(String)