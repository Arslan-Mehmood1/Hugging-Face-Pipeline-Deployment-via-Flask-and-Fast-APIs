from flask import Flask, request, jsonify
from transformers import pipeline

sentiment_analysis_pipeline = pipeline(task="sentiment-analysis",
                                       model="distilbert-base-uncased-finetuned-sst-2-english")

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Sentence Sentiment Analysis Using HuggingFace Pipeline, deployed via Flask API!</h2>"

@app.route("/predict", methods=["POST"])
def predict():
    result = sentiment_analysis_pipeline(request.json[0])
    return jsonify({"Sentiment" : f"{result[0]['label']}"})

if __name__ == '__main__':
    app.run(debug=False, port=8080, host="0.0.0.0")