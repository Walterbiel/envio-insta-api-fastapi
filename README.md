# API com FastAPI

Material gratuito do QG da Engenharia de Dados. Você recebeu porque comentou **API**.

Uma API REST completa de produtos: cadastrar, listar, buscar, atualizar e apagar.

## Como usar este material

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Suba a API:

```bash
uvicorn app.main:app --reload
```

3. Abra no navegador → [http://localhost:8000/docs](http://localhost:8000/docs)
4. Teste cada rota pelo botão **Try it out**

## O fluxo

```
Requisição → main.py (rotas) → schemas.py (valida) → models.py → SQLite (produtos.db)
```

## Estrutura

```
app/
  database.py → conexão com o banco
  models.py   → tabela do banco (SQLAlchemy)
  schemas.py  → formato de entrada e saída (Pydantic)
  main.py     → as rotas da API
```

## Rotas

| Método | Rota | O que faz |
|---|---|---|
| POST | `/produtos` | Cadastra |
| GET | `/produtos` | Lista todos |
| GET | `/produtos/{id}` | Busca um |
| PUT | `/produtos/{id}` | Atualiza |
| DELETE | `/produtos/{id}` | Apaga |

## Testando pelo terminal

```bash
curl -X POST http://localhost:8000/produtos -H "Content-Type: application/json" -d "{\"nome\": \"Mouse\", \"preco\": 80}"
curl http://localhost:8000/produtos
```

## O que observar

→ Preço negativo é recusado → validação no `schemas.py`
→ Produto que não existe → erro 404
→ Documentação gerada sozinha em `/docs`

## Desafio

Adicione um filtro `GET /produtos?preco_max=100`.

## Material completo

[fastAPI_template](https://github.com/Walterbiel/fastAPI_template)

## QG da Engenharia de Dados

Este material é uma amostra do que você encontra no QG.

→ Trilha completa do zero ao sênior
→ Projetos reais para o portfólio
→ Comunidade para tirar dúvidas

Acesse → [qg-engenharia-de-dados.com.br](https://qg-engenharia-de-dados.com.br)
YouTube → [@gonzagadosdados](https://www.youtube.com/@gonzagadosdados)
