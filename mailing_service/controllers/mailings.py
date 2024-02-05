from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from models.core import Mailing
from models.schemas import MailingCreate, MailingUpdate


async def get_mailing_db(db: AsyncSession, mailing_id: int):
    mailing = await db.scalar(select(Mailing).where(Mailing.id == mailing_id))
    if not mailing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Mailing id: '{mailing_id}' not found!"
        )
    return mailing


async def create_mailing_db(db: AsyncSession, mailing_data: MailingCreate):
    if mailing_data.start_mailing >= mailing_data.stop_mailing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Datetime of start mailing should be before the end of mailing"
        )
    mailing = Mailing()
    mailing.start_mailing = mailing_data.start_mailing
    mailing.stop_mailing = mailing_data.stop_mailing
    mailing.text = mailing_data.text
    mailing.tag = mailing_data.tag
    mailing.operator_code = mailing_data.operator_code
    db.add(mailing)
    await db.commit()
    return {
        "id": mailing.id,
        "start_mailing": mailing.start_mailing,
        "stop_mailing": mailing.stop_mailing
    }


async def update_mailing_db(db: AsyncSession, mailing_data: MailingUpdate):
    mailing = await db.scalar(select(Mailing).where(Mailing.id == mailing_data.id))
    if not mailing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Mailing id '{mailing_data.id}' not found!"
        )
    for name, value in mailing_data.model_dump(exclude_unset=True).items():
        setattr(mailing, name, value)
    if mailing.start_mailing >= mailing.stop_mailing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Datetime of start mailing should be before the end of mailing"
        )
    await db.commit()
    return {
        "id": mailing.id,
        "start_mailing": mailing.start_mailing,
        "stop_mailing": mailing.stop_mailing,
        "text": mailing.text,
        "tag": mailing.tag,
        "operator_code": mailing.operator_code
    }


async def delete_mailing_db(db: AsyncSession, mailing_id: int):
    mailing = await db.scalar(select(Mailing).where(Mailing.id == mailing_id))
    if not mailing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Mailing id: '{mailing_id}' not found!"
        )
    await db.delete(mailing)
    await db.commit()
