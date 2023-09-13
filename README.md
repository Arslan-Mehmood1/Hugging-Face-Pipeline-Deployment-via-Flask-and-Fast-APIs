# HuggingFace pipelines deployment

## Sentiment-Analysis Pipeline Deployment
- model = distilbert-base-uncased-finetuned-sst-2-english
- task = sentiment-analysis

### 1) FastAPI
The `fast_api.py` contains the code for deployment via FastAPI.

#### Start API
```bash
uvicorn --host 0.0.0.0 fast_api:app
```
#### Inference Example
```python
curl -X POST -H "Content-Type: application/json" -d '{"text":"a beautiful rainy day."}' http://localhost:8000/predict
```

### 2) Flask API
The `flask_api.py` contains the code for deployment via Flask API.
#### Start API
```bash
python flask_api.py
```

#### Inference Example
```python
curl -X POST -H "Content-Type: application/json" -d '["a beautiful rainy day."]' http://localhost:8080/predict
```
