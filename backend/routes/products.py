from fastapi import APIRouter, HTTPException
from typing import List, Dict

router = APIRouter()

products = [
    {"id": 1, "name": "Товар 1", "price": 10},
    {"id": 2, "name": "Товар 2", "price": 20}
]

@router.get("/", response_model=List[Dict])
async def get_products():
    return products


@router.get("/{id}", response_model=Dict)
async def get_product(id: int):
    product = next((item for item in products if item["id"] == id), None)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Товар не найден")
