import os
import motor.motor_asyncio as motor
import config

client = motor.AsyncIOMotorClient(config.datasource_host, config.datasource_port)
db = client["lista_de_tarefas"]
collection = db["tarefas"]

