import smtplib
from email.mime.text import MIMEText
from utils.logger import logger
from fastapi import HTTPException
import os

from dotenv import load_dotenv
#load_dotenv()


SENDER = os.getenv("SENDER")
PASSWORD = os.getenv("SENDER_PASSWORD")
SMTP = os.getenv("SMTP")
PORT = os.getenv("PORT")



def trans_start_email(email: str, name: str, operator_name: str):
    subject = "Proceso de transferencia iniciado"
    body = f"""Hola {name},
    
    Te informamos que se ha iniciado tu proceso de transferencia al operador {operator_name}.

    Este proceso será completado una vez el nuevo operador confirme la recepción de tu información, adicionalmente, Oreo te informa que el operador no puede garantizar la transferencia de ningun documento subido al sistema despues del inicio del proceso.

    Gracias por hacer parte del operador Oreo.

    Saludos,
    Equipo Oreo"""
    
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = email

    logger.info(f"{msg},{PASSWORD},{SMTP},{SENDER},{PORT}")

    try:
        with smtplib.SMTP(SMTP, PORT) as server:
        
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, [email], msg.as_string())
        logger.info(f"Correo enviado a {email}")
        return
    except Exception as e:
        logger.error(f"Error enviando correo a {email}: {e}")
        raise HTTPException(status_code=502, detail="No se pudo enviar el correo de bienvenida.")
    


def transfer_failed_email(email: str, name: str):
    subject = "Proceso de transferencia iniciado"
    body = f"""Hola {name},
    
    parece que tu nuevo operador tuvo miedo al compromiso. No te preocupes, aquí siempre serás bienvenido 😉
    
    
    Saludos,
    Equipo Oreo"""
    
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = email

    logger.info(f"{msg},{PASSWORD},{SMTP},{SENDER},{PORT}")

    try:
        with smtplib.SMTP(SMTP, PORT) as server:
        
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, [email], msg.as_string())
        logger.info(f"Correo enviado a {email}")
        return
    except Exception as e:
        logger.error(f"Error enviando correo a {email}: {e}")
        raise HTTPException(status_code=502, detail="No se pudo enviar el correo de bienvenida.")
    


def transfer_success_email(email: str, name: str):
    subject = "Proceso de transferencia iniciado"
    body = f"""Hola {name},
    
    tu transferencia al nuevo operador ha sido completada exitosamente. ¡Te deseamos lo mejor!

    Saludos,
    Equipo Oreo"""
    
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = email

    logger.info(f"{msg},{PASSWORD},{SMTP},{SENDER},{PORT}")

    try:
        with smtplib.SMTP(SMTP, PORT) as server:
        
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, [email], msg.as_string())
        logger.info(f"Correo enviado a {email}")
        return
    except Exception as e:
        logger.error(f"Error enviando correo a {email}: {e}")
        raise HTTPException(status_code=502, detail="No se pudo enviar el correo de bienvenida.")