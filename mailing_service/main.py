from fastapi import FastAPI

from routers.clients import router as client_routers
from routers.mailings import router as mailing_routers
from routers.execute_mailing import router as execute_mailing_routers

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
    router=execute_mailing_routers,
    prefix='/execute_mailing'
)