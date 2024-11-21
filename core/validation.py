from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    dob: datetime
    address: str
    gender: str
    email: str
    phone_number: int

    @classmethod
    def validation(cls, user):
        cls.validate_email(user.email)
        cls.validate_phone_number(user.phone_number)
        cls.validate_gender(user.gender)
        cls.validate_dob(user.dob)

    @classmethod
    def validate_email(cls, email):
        if "@" not in email:
            raise ValueError("Invalid email address")

    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(str(phone_number)) != 10:
            raise ValueError("Invalid phone number")
        return True

    @classmethod
    def validate_gender(cls, gender):
        if gender not in ["Male", "Female"]:
            raise ValueError("Invalid gender")
        return True

    @classmethod
    def validate_dob(cls, dob):
        if dob > datetime.now():
            raise ValueError("Invalid date of birth")

        if dob.year < 1930:  # change if needed
            raise ValueError("Invalid date of birth")
        return True
