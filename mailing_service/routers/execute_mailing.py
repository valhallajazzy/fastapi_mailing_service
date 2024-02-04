from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..controllers.execute_mailing import get_execute_mailing

router = APIRouter

@router.get('/{mailing_id}', status_code=200)
def execute_mailing(mailing_id: int, db: Session = Depends(get_db)):
    return get_execute_mailing(db=db, mailing_id=mailing_id)