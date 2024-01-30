from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from models.core import Client
from models.schemas import ClientBase
import phonenumbers


def get_client_db(db: Session, client_id: int):
    if not db.scalar(select(Client).where(Client.id == client_id)):
        raise HTTP_400_BAD_REQUEST
    client = db.scalar(select(Client).where(Client.id == client_id))
    return client


def register_client_db(db: Session, client_data: ClientBase):
    if db.scalar(select(Client).where(Client.phone_number == client_data.phone_number)):
        raise HTTP_400_BAD_REQUEST
    operator_code = str(phonenumbers.parse(client_data.phone_number).national_number)[:3]
    client = Client(phone_number=client_data.phone_number)
    client.operator_code = int(operator_code)
    client.tag = client_data.tag
    client.time_zone = client_data.time_zone
    db.add(client)
    db.commit()
    return {
        "id": client.id,
        "phone_number": client.phone_number
    }