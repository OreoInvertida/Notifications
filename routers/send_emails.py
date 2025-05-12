from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from services.mail_service import send_welcome_email, send_transfer_email, req_int_documents_email, req_ext_documents_email
from services.transfer_mail_service import trans_start_email, transfer_failed_email, transfer_success_email
from fastapi import HTTPException
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
#load_dotenv()
from services.token_service import verify_token
from models.models import CreateReqEmail, EmailRequest, Transfer, DocumentTransferRequest, UserOutTranStart

router = APIRouter()



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
    

# @router.post("/documents")
# def send_document_links(data: DocumentTransferRequest, payload: dict = Depends(verify_token)):
#     try:
#         send_documents_email(data.email, data.name, data.links)
#         return {"message": "Correo con enlaces de documentos enviado exitosamente."}
#     except HTTPException as e:
#         raise e
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


@router.post("/send_req_int")
def send_req_int_email(data: CreateReqEmail):

    try:
        req_int_documents_email(data=data)
            
        return {"message": f"Correo req_int enviado a {data.solicited_email}"}
    except Exception as e:
        raise e
    

@router.post("/send_req_ext")
def send_req_ext_email(data: CreateReqEmail):

    try:
        req_ext_documents_email(data=data)
            
        return {"message": f"Correo req_ext enviado a {data.solicited_email}"}
    except Exception as e:
        raise e
    

@router.post("/send_trans_start")
def send_trans_start_email(data: UserOutTranStart):

    try:
        trans_start_email(data=data)
            
        return {"message": f"Correo trans_start enviado a {data.email}"}
    except Exception as e:
        raise e
    

@router.post("/transfer_succes")
def send_trans_succ_email(data: EmailRequest):

    try:
        transfer_success_email(email=data.email, name=data.name)
            
        return {"message": f"Correo trans_start enviado a {data.email}"}
    except Exception as e:
        raise e



@router.post("/transfer_failed")
def send_trans_fail_email(data: EmailRequest):

    try:
        transfer_failed_email(email=data.email, name=data.name)
            
        return {"message": f"Correo trans_start enviado a {data.email}"}
    except Exception as e:
        raise e