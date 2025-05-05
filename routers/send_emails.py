from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from services.mail_service import send_welcome_email

router = APIRouter()

class EmailRequest(BaseModel):
    email: EmailStr
    name: str

@router.post("/send")
async def send_email(data: EmailRequest):
    await send_welcome_email(data.email, data.name)
    return {"message": f"Correo enviado a {data.email}"}
