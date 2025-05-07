import smtplib
from email.mime.text import MIMEText
from utils.logger import logger
from fastapi import HTTPException
import os

from dotenv import load_dotenv
#load_dotenv()


SENDER = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("SENDER_PASSWORD")
SMTP = os.getenv("SMTP")
PORT = os.getenv("PORT")



def send_welcome_email(email: str, name: str):
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
        return
    except Exception as e:
        logger.error(f"Error enviando correo a {email}: {e}")
        raise HTTPException(status_code=502, detail="No se pudo enviar el correo de bienvenida.")
    

def send_transfer_email(email: str, name: str, reset_link: str):
    subject = "Bienvenido a tu nuevo operador: Oreo"
    body = f"""Hola {name},

Nos alegra darte la bienvenida a tu nuevo operador ciudadano: Oreo.

Para finalizar tu proceso de transferencia, por favor cambia tu contraseña en el siguiente enlace:
{reset_link}

¡Bienvenido a Oreo!
Equipo Oreo"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = email

    try:
        with smtplib.SMTP(SMTP, PORT) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, [email], msg.as_string())
        logger.info(f"Correo de transferencia enviado a {email}")
    except Exception as e:
        logger.error(f"⛔ Error enviando correo de transferencia a {email}: {e}")
        raise HTTPException(status_code=502, detail="No se pudo enviar el correo de transferencia.")


def send_documents_email(email: str, name: str, links: list[str]):
    subject = "📄 Documentos de transferencia disponibles para descargar"
    links_formatted = "\n".join([f"- {link}" for link in links])

    body = f"""Hola {name},

Te informamos que se te han transferido documentos a tu cuenta. Puedes descargarlos durante los próximos 7 días desde los siguientes enlaces:

{links_formatted}

Después de ese tiempo, los enlaces expirarán automáticamente.

Saludos,
Equipo Oreo"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = email

    try:
        with smtplib.SMTP(SMTP, PORT) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, [email], msg.as_string())
        logger.info(f"Correo de documentos enviado a {email}")
    except Exception as e:
        logger.error(f"⛔ Error enviando correo de documentos a {email}: {e}")
        raise HTTPException(status_code=502, detail="No se pudo enviar el correo con enlaces de documentos.")
