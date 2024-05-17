from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Atleta(BaseModel):
    nome: Annotated[str, Field(description="Nome do atleta", examples='Kevin', max_length=50)]
    cpf: Annotated[str, Field(description="cpf do atleta", examples='1234567891011', max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", examples=23)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", examples=90.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", examples=1.70)]
    genero: Annotated[str, Field(description="Genero do atleta", examples="M", max_length=1)]