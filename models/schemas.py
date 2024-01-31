from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import field_validator
from pytz import all_timezones
from datetime import datetime

PhoneNumber.supported_regions = "RU"
PhoneNumber.phone_format = 'E164'
PhoneNumber.min_length = 11
PhoneNumber.max_length = 12


class ClientBase(BaseModel):
    phone_number: PhoneNumber


class ClientCreate(ClientBase):
    tag: str | None = None
    time_zone: str

    @field_validator('time_zone')
    def verify_time_zone(cls, time_zone):
        if time_zone not in all_timezones:
            raise ValueError('Incorrect timezone')
        return time_zone


class ClientUpdate(ClientBase):
    tag: str | None = None
    time_zone: str | None = None

    @field_validator('time_zone')
    def verify_time_zone(cls, time_zone):
        if time_zone not in all_timezones:
            raise ValueError("Incorrect timezone")
        return time_zone


class MailingBase(BaseModel):
    tag: str | None = None
    operator_code: int | None = None

    @field_validator('operator_code')
    def verify_operator_code(cls, operator_code):
        if operator_code < 100 or operator_code > 1000:
            raise ValueError("Incorrect operator's code")
        return operator_code


class MailingCreate(MailingBase):
    start_mailing: datetime
    stop_mailing: datetime
    text: str

    @field_validator('operator_code')
    def verify_operator_code(cls, operator_code):
        if operator_code < 100 or operator_code > 1000:
            raise ValueError("Incorrect operator's code")
        return operator_code


class MailingUpdate(MailingBase):
    id: int
    start_mailing: datetime = None
    stop_mailing: datetime = None
    text: str = None



