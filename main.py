from fastapi import FastAPI

from routers.clients import router as client_routers


app = FastAPI()


app.include_router(
    router=client_routers,
    prefix='/clients'
)