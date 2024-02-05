from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from models.core import Client
from models.schemas import ClientCreate, ClientUpdate, ClientBase
import phonenumbers


async def get_client_db(db: AsyncSession, client_id: int):
    client = await db.scalar(select(Client).where(Client.id == client_id))
    if not client:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Client id: '{client_id}' not found!"
        )
    return client


async def create_client_db(db: AsyncSession, client_data: ClientCreate):
    if await db.scalar(select(Client).where(Client.phone_number == client_data.phone_number)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Phone {client_data.phone_number} already exist!"
        )
    operator_code = str(phonenumbers.parse(client_data.phone_number).national_number)[:3]
    client = Client(phone_number=client_data.phone_number)
    client.operator_code = int(operator_code)
    client.tag = client_data.tag
    client.time_zone = client_data.time_zone
    db.add(client)
    await db.commit()
    return {
        "id": client.id,
        "phone_number": client.phone_number
    }


async def update_client_db(db: AsyncSession, client_data: ClientUpdate):
    client = await db.scalar(select(Client).where(Client.phone_number == client_data.phone_number))
    if not client:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Phone {client_data.phone_number} not found!"
        )
    for name, value in client_data.model_dump(exclude_unset=True).items():
        setattr(client, name, value)
    await db.commit()
    return {
        "phone_number": client.phone_number,
        "tag": client.tag,
        "time_zone": client.time_zone,
    }


async def delete_client_db(db: AsyncSession, client_data: ClientBase):
    client = await db.scalar(select(Client).where(Client.phone_number == client_data.phone_number))
    if not client:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Phone {client_data.phone_number} not found!"
        )
    await db.delete(client)
    await db.commit()

