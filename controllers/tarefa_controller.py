
from models import tarefa
from fastapi import APIRouter, status

tarefa_model = tarefa.Tarefa
router = APIRouter()


@router.get("/tarefas", status_code=status.HTTP_200_OK)
async def listar_tarefas() -> tarefa:
    return {"mensagem": "Olá Mundo"}


@router.get("/tarefas/{id}", status_code=status.HTTP_200_OK)
async def buscar_tarefa_por_id(id: str):
    return {"mensagem": "Olá Mundo"}


@router.post("/tarefas", status_code=status.HTTP_200_OK)
async def inserir_tarefa(tarefa: tarefa_model):
    return tarefa
''
