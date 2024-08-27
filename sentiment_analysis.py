from transformers import pipeline

# Initialize sentiment analysis pipeline with a model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline('sentiment-analysis', model=model_name)

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result[0]['label']
