from fastapi import FastAPI
import os
from dotenv import load_dotenv
from routes import products

load_dotenv()

app= FastAPI()
app.include_router(products.router, prefix="/products") 

@app.get("/")
async def root():
    return {"message": "Start project"}

