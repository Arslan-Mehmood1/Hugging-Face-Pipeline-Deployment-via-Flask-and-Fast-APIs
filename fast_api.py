from transformers import pipeline
from fastapi import FastAPI, Response
from pydantic import BaseModel

sentiment_analysis_pipeline = pipeline(task="sentiment-analysis",
                                       model="distilbert-base-uncased-finetuned-sst-2-english")

app = FastAPI()

class Body(BaseModel):
    text:str

@app.get('/')
def root():
    return "<h2>Welcome to Sentiment Analysis Using HuggingFace Pipelines, deployed via FastAPI</h2>"

@app.post('/predict')
def predict(body: Body):
    result = sentiment_analysis_pipeline(body.text)

    return {"Sentiment" : f"{result[0]['label']}"}
