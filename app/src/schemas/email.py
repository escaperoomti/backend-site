import dns.resolver
from pydantic import BaseModel, EmailStr, field_validator


class EmailSchema(BaseModel):
    email: EmailStr

    @field_validator("email")
    @classmethod
    def mx_validator(cls, v: str) -> str:
        domain = v.split("@")[-1]
        try:
            dns.resolver.resolve(domain, "MX")
        except dns.resolver.NoAnswer:
            raise ValueError("Domain does not have a MX record")
        return v
