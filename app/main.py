from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import models
from app.database import Base, engine, get_db
from app.schemas import ProdutoEntrada, ProdutoSaida

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Produtos", description="Material do QG da Engenharia de Dados")


def buscar_ou_404(db: Session, produto_id: int) -> models.Produto:
    produto = db.get(models.Produto, produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.post("/produtos", response_model=ProdutoSaida, status_code=201)
def criar(dados: ProdutoEntrada, db: Session = Depends(get_db)):
    produto = models.Produto(**dados.model_dump())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto


@app.get("/produtos", response_model=list[ProdutoSaida])
def listar(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()


@app.get("/produtos/{produto_id}", response_model=ProdutoSaida)
def buscar(produto_id: int, db: Session = Depends(get_db)):
    return buscar_ou_404(db, produto_id)


@app.put("/produtos/{produto_id}", response_model=ProdutoSaida)
def atualizar(produto_id: int, dados: ProdutoEntrada, db: Session = Depends(get_db)):
    produto = buscar_ou_404(db, produto_id)
    produto.nome = dados.nome
    produto.preco = dados.preco
    db.commit()
    db.refresh(produto)
    return produto


@app.delete("/produtos/{produto_id}", status_code=204)
def apagar(produto_id: int, db: Session = Depends(get_db)):
    produto = buscar_ou_404(db, produto_id)
    db.delete(produto)
    db.commit()
