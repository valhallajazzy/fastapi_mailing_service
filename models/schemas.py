from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import field_validator
from pytz import all_timezones

PhoneNumber.supported_regions = "RU"
PhoneNumber.phone_format = 'E164'
PhoneNumber.min_length = 11
PhoneNumber.max_length = 12


class ClientBase(BaseModel):
    phone_number: PhoneNumber


class ClientCreate(ClientBase):
    tag: str
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
            raise ValueError('Incorrect timezone')
        return time_zone


