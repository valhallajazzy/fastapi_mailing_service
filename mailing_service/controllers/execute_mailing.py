from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import Response

from models.core import Mailing
from models.schemas import MailingCreate, MailingUpdate


def get_execute_mailing(db: Session, mailing_id: int):
    mailing = db.scalar(select(Mailing).where(Mailing.id == mailing_id))
    if not mailing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Mailing id: '{mailing_id}' not found!"
        )
    return Response('Your request has been accepted', status_code=200)


