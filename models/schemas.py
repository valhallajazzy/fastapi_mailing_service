from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import EmailStr, field_validator
from pytz import all_timezones

PhoneNumber.supported_regions = "RU"
PhoneNumber.phone_format = 'E164'
PhoneNumber.min_length = 11
PhoneNumber.max_length = 12


class ClientBase(BaseModel):
    phone_number: PhoneNumber
    tag: str
    time_zone: str

    # @field_validator('operator_code')
    # def verify_length_mobile_code(cls, mobile_code):
    #     if mobile_code < 100 or mobile_code > 999:
    #         raise ValueError('Incorrect mobile code')
    #     return mobile_code

    @field_validator('time_zone')
    def verify_time_zone(cls, time_zone):
        if time_zone not in all_timezones:
            raise ValueError('Incorrect timezone')
        return time_zone

