from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from models import schemas
from models.database import get_db
from controllers.mailings import get_mailing_db, create_mailing_db, update_mailing_db, delete_mailing_db


router = APIRouter()


@router.get('/{mailing_id}', status_code=200)
def get_mailing(mailing_id: int, db: Session = Depends(get_db)):
    return get_mailing_db(db=db, mailing_id=mailing_id)


@router.post('/create', status_code=201)
def create_mailing(mailing_data: schemas.MailingCreate, db: Session = Depends(get_db)):
    return create_mailing_db(db=db, mailing_data=mailing_data)


@router.patch('/update', status_code=200)
def update_mailing(mailing_data: schemas.MailingUpdate, db: Session = Depends(get_db)):
    return update_mailing_db(db=db, mailing_data=mailing_data)


@router.delete('/delete/{mailing_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_mailing(mailing_id: int, db: Session = Depends(get_db)):
    return delete_mailing_db(db=db, mailing_id=mailing_id)