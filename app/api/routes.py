from fastapi import FastAPI
from app.services.converter import convert_currency
from fastapi import Query
from fastapi import APIRouter

router = APIRouter()

@router.get("/convert")
def convert(from_currency: str = Query(...), to_currency: str = Query(...), amount: float = Query(...)):
    result = convert_currency(from_currency, to_currency, amount)
    return result