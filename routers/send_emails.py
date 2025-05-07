from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from services.mail_service import send_welcome_email
from fastapi import HTTPException
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

class EmailRequest(BaseModel):
    email: EmailStr
    name: str


@router.post("/send")
def send_email(data: EmailRequest):

    try:
        send_welcome_email(data.email, data.name)
            
        return {"message": f"Correo enviado a {data.email}"}
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))