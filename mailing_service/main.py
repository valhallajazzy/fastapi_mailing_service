from fastapi import FastAPI

from routers.clients import router as client_routers
from routers.mailings import router as mailing_routers

app = FastAPI()


app.include_router(
    router=client_routers,
    prefix='/clients'
)

app.include_router(
    router=mailing_routers,
    prefix='/mailing'
)

app.include_router(
    router=...,
    prefix=...
)