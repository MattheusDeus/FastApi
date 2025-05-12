from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Tarefa(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False

tarefas = []


@app.post("/tarefas")
async def criar_tarefa(tarefa:Tarefa):
    tarefas.append(tarefa)
    return tarefa

@app.get("/tarefas")
async def listar_tarefas():
    return {"Todas as tarefas sendo listadas": tarefas}

@app.get("/tarefas/{id}", response_model=Tarefa)
async def listar_tarefa_especifica(id:int):
    if id < 0 or id  >=len(tarefas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefas[id]


@app.put("/tarefas/{id}", response_model=Tarefa)
async def alterar_tarefa(id: int, tarefa: Tarefa):
    if id  < 0 or id >= len(tarefas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    tarefas[id] = tarefa
    return tarefa

@app.delete("/tarefa/{id}", status_code=204)
async def deletar_tarefa(id: int):
    if id  < 0 or id >= len(tarefas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    tarefas.pop(id)
    return tarefas

