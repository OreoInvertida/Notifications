from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict
from datetime import datetime

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

class CreateReqEmail(BaseModel):
    solicitant_email: str
    solicitant_name: str
    solicited_email: str
    solicited_name: str
    documents: list[str]