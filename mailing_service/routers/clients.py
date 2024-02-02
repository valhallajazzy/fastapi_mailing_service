from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from models import schemas
from models.database import get_db
from controllers.clients import create_client_db, get_client_db, update_client_db, delete_client_db

router = APIRouter()


@router.get('/{client_id}', status_code=200)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return get_client_db(db=db, client_id=client_id)


@router.post('/create', status_code=201)
def create_client(client_data: schemas.ClientCreate, db: Session = Depends(get_db)):
    return create_client_db(db=db, client_data=client_data)


@router.patch('/update', status_code=200)
def update_client(client_data: schemas.ClientUpdate, db: Session = Depends(get_db)):
    return update_client_db(db=db, client_data=client_data)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_data: schemas.ClientBase, db: Session = Depends(get_db)):
    return delete_client_db(client_data=client_data, db=db)