from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from models import schemas
from models.database import get_db
from controllers.clients import create_client_db, get_client_db, update_client_db, delete_client_db

router = APIRouter()


@router.get('/{client_id}', status_code=200)
async def get_client(client_id: int, db: AsyncSession = Depends(get_db)):
    return await get_client_db(db=db, client_id=client_id)


@router.post('/create', status_code=201)
async def create_client(client_data: schemas.ClientCreate, db: AsyncSession = Depends(get_db)):
    return await create_client_db(db=db, client_data=client_data)


@router.patch('/update', status_code=200)
async def update_client(client_data: schemas.ClientUpdate, db: AsyncSession = Depends(get_db)):
    return await update_client_db(db=db, client_data=client_data)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(client_data: schemas.ClientBase, db: AsyncSession = Depends(get_db)):
    return await delete_client_db(client_data=client_data, db=db)