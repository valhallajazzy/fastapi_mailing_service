from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from typing import Optional
from datetime import datetime
import enum


class Base(DeclarativeBase):
    pass


class SendingStatus(enum.Enum):
    sent = "sent"
    not_sent = "not_sent"
    sending_error = "sending_error"


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    operator_code: Mapped[int]
    tag: Mapped[Optional[str]]
    time_zone: Mapped[str]

    messages: Mapped[list["Message"]] = relationship(
        back_populates="client"
    )


class Mailing(Base):
    __tablename__ = "mailings"

    id: Mapped[int] = mapped_column(primary_key=True)
    start_mailing: Mapped[datetime]
    stop_mailing: Mapped[datetime]
    text: Mapped[str]
    tag: Mapped[Optional[str]]
    operator_code: Mapped[Optional[int]]

    messages: Mapped[list["Message"]] = relationship(
        back_populates="mailing"
    )


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    status: Mapped[SendingStatus]

    id_mailing: Mapped[int] = mapped_column(ForeignKey("mailings.id", ondelete="CASCADE"))
    mailing: Mapped[list["Mailing"]] = relationship(
        back_populates="messages"
    )

    id_client: Mapped[int] = mapped_column(ForeignKey("clients.id", ondelete="CASCADE"))
    client: Mapped[list["Client"]] = relationship(
        back_populates="messages"
    )


