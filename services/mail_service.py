import smtplib
from email.mime.text import MIMEText
from utils.logger import logger
from fastapi import HTTPException

from dotenv import load_dotenv
import os

load_dotenv()

SENDER = os.getenv("SENDER")
PASSWORD = os.getenv("PASSWORD")
SMTP = os.getenv("SMTP")
PORT = os.getenv("PORT")


async def send_welcome_email(email: str, name: str):
    subject = "Bienvenido al Operador Oreo"
    body = f"Hola {name},\n\nTu cuenta ha sido creada exitosamente dentro del operador Oreo.\n\nBienvenido!!\nEquipo Oreo"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = email

    try:
        with smtplib.SMTP(SMTP, PORT) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, [email], msg.as_string())
        logger.info(f"Correo enviado a {email}")
    except Exception as e:
        logger.error(f"⛔ Error enviando correo a {email}: {e}")
        raise HTTPException(status_code=502, detail="No se pudo enviar el correo de bienvenida.")
