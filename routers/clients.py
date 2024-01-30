from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import schemas
from models.database import get_db
from controllers.users import register_client_db, get_client_db

router = APIRouter()


@router.get('/{client_id}', status_code=200)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return get_client_db(db=db, client_id=client_id)


@router.post('/register', status_code=201)
def register_client(client_data: schemas.ClientBase, db: Session = Depends(get_db)):
    return register_client_db(db=db, client_data=client_data)
