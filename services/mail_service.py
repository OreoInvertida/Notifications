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



def send_welcome_email(email: str, name: str):
    subject = "Bienvenido al Operador Oreo"
    body = f"Hola {name},\n\nTu cuenta ha sido creada exitosamente dentro del operador Oreo.\n\nBienvenido!!\nEquipo Oreo"

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
        raise e


#####DIVVV



def req_int_documents_email(data: dict):
    subject = "📄 Documentos solicitados para transferencia"
    body = f"""Hola {data.solicited_name},

Te informamos que se te ha solicitado una transferencia de documentos a tu cuenta de oreo por parte de otro usuario. Te invitamos a acceder a la aplicación para mas información.

Saludos,
Equipo Oreo"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = data.solicited_email

    try:
        with smtplib.SMTP(SMTP, PORT) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, [data.solicited_email], msg.as_string())
        logger.info(f"Correo de documentos enviado a {data.solicited_email}")
    except Exception as e:
        logger.error(f"⛔ Error enviando correo de documentos a {data.solicited_email}: {e}")
        raise e

def req_ext_documents_email(data: dict):
    print(data)
    subject = "📄 Documentos solicitados para transferencia"
    body = f"""Hola {data.solicited_name},

Te informamos que se te ha solicitado una transferencia de documentos por parte de un usuario de la plataforma Oreo. A continuación encontraras la información relevante.

Usuario solicitante: {data.solicitant_name}
Correo del usuario: {data.solicitant_email}
Documentos solicitados: {data.documents}

Saludos,
Equipo Oreo"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = data.solicited_email

    try:
        with smtplib.SMTP(SMTP, PORT) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, [data.solicited_email], msg.as_string())
        logger.info(f"Correo de documentos enviado a {data.solicited_email}")
    except Exception as e:
        logger.error(f"⛔ Error enviando correo de documentos a {data.solicited_email}: {e}")
        raise e







def send_int_documents_email(email: str, name: str, links: list[str]):
    subject = "📄 Documentos de transferencia disponibles para descargar"
    links_formatted = "\n".join([f"- {link}" for link in links])

    body = f"""Hola {name},

Te informamos que se ha completado una transferencia de documentos a tu cuenta. A partir de ahora podras acceder a ellos desde la plataforma y adicionalmente podras descargarlos desde el/los siguientes enlace(s) durante los próximos 7 días:

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
        raise e
    

def send_ext_documents_email(email: str, name: str, links: list[str]):
    subject = "📄 Documentos de transferencia disponibles para descargar"
    links_formatted = "\n".join([f"- {link}" for link in links])

    body = f"""Hola {name},

Te informamos que un usuario de Oreo te ha transferido documentos desde su cuenta. Puedes descargarlos durante los próximos 7 días desde los siguientes enlaces:

{links_formatted}

Después de ese tiempo, los enlaces expirarán automáticamente.

Para mas facilidad durante este proceso y muchas mas ventajas considera inscribirte a Oreo Invertida, el mejor operador de carpeta ciudadana!!

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
        raise e