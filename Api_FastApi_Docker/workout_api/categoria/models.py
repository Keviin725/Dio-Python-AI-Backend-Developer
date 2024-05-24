from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String


class CategoriaModal(BaseModel):
    __tablename__ = 'Categorias'
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atleta: Mapped['AtletaModal'] = relationship(back_populates='categoria')
    