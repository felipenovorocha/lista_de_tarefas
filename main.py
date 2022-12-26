from fastapi import FastAPI
from controllers import tarefa_controller

app = FastAPI(title="POC TodoList",
              description="Api criada para testes de criação de serviço em Fast Api",
              openapi_url="/openapi.json",
              docs_url="/docs",
              redoc_url="/redoc")


@app.get("/", tags=["Links"])
async def seja_bem_vindo():

    links = [{"swagger": "/docs"}, {"swagger-alt": "/redoc"}]

    return {"Links": links}


@app.on_event("startup")
async def startup():
    app.include_router(tarefa_controller.router,
                       prefix="/v1", tags=["Tarefas"])

    return app
