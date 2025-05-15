from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="Currency Converter API")

app.include_router(routes.router)

