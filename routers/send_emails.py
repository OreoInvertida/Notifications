from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from services.mail_service import send_welcome_email, send_transfer_email, send_documents_email
from fastapi import HTTPException
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
#load_dotenv()
from services.token_service import verify_token

router = APIRouter()

class EmailRequest(BaseModel):
    email: EmailStr
    name: str

class Transfer(BaseModel):
    email: str
    name: str
    reset_link: str

class DocumentTransferRequest(BaseModel):
    email: str
    name: str
    links: list[str]


@router.post("/send")
def send_email(data: EmailRequest):

    try:
        send_welcome_email(data.email, data.name)
            
        return {"message": f"Correo enviado a {data.email}"}
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    
@router.post("/transfer")
def welcome_transfer_user(data: Transfer, payload: dict = Depends(verify_token)):
    try:
        send_transfer_email(data.email, data.name, data.reset_link)
        return {"message": "Correo de bienvenida enviado exitosamente."}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    

@router.post("/documents")
def send_document_links(data: DocumentTransferRequest, payload: dict = Depends(verify_token)):
    try:
        send_documents_email(data.email, data.name, data.links)
        return {"message": "Correo con enlaces de documentos enviado exitosamente."}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
