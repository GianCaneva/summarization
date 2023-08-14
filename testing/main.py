#To install
#pip3 install fastapi
#pip3 install uvicorn
#pip3 install pydantic
#To run: 
#python3 -m uvicorn main:app --reload --port 50000

from fastapi import FastAPI
from transformers import pipeline
summarizer = pipeline("summarization", model="ELiRF/mt5-base-dacsa-es")

app = FastAPI()

@app.post('/sum', status_code=201)
def create_sum(text: str):
    return summarizer(text, max_length=400, min_length=300, do_sample=False)


