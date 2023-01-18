from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from infra.config.database import buscar, atualizaSitEmail, conectar, close, inserindoEmail, buscarsituacao
from infra.repositorios.repositoriosFuncs import validaCampo, validaCampoEmail, validaEmail, enviaremail


app = FastAPI()

class requisicaoEmail(BaseModel):
    chave: int
    assunto: str
    texto: str
    endereco: str

lista: List[requisicaoEmail] = []

@app.post('/listar')
def criar_requisicao(requisicaoEmail: requisicaoEmail):
    lista.append(requisicaoEmail)
    return lista

@app.get('/listar')
def listar_emaail():
    return "Legal, conectou!"


