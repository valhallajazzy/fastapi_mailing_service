from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from models.core import Mailing


async def get_execute_mailing(db: AsyncSession, mailing_id: int):
    mailing = await db.scalar(select(Mailing).where(Mailing.id == mailing_id))
    if not mailing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Mailing id: '{mailing_id}' not found!"
        )

    return {
        'detail': 'Your task is accepted'
    }


