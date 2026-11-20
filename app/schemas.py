from pydantic import BaseModel, ConfigDict, Field


class ProdutoEntrada(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    preco: float = Field(gt=0)   # recusa preço zero ou negativo


class ProdutoSaida(ProdutoEntrada):
    model_config = ConfigDict(from_attributes=True)
    id: int
