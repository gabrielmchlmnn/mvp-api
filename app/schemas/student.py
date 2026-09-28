from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    zip_code: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True