from fastapi import FastAPI, Query
from pydantic import BaseModel

from src.summarizer import summarize

class Item(BaseModel):
    text: str

app = FastAPI()

@app.get('/')
async def index(q: str = Query(None)):
    return summarize(q)

@app.post("/summarize")
async def annotate(item: Item):
    return summarize(item.text)