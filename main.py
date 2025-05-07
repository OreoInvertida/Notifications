from fastapi import FastAPI
from routers.send_emails import router as email_router

app = FastAPI(title="Notifications Microservice")
app.include_router(email_router, tags=["Notifications"])
