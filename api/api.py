from flask import Flask, request, make_response
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from multiprocessing import Process

app = Flask(__name__)

# Configurer l'API de Toxicité
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained("FredZhang7/one-for-all-toxicity-v3")
model = AutoModelForSequenceClassification.from_pretrained("FredZhang7/one-for-all-toxicity-v3").to(device)

# Configurer l'API de Sentiment
distilled_student_sentiment_classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    top_k=None
)

# Route pour prédire la toxicité
@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=208,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )
    input_ids = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=1).item()

    response = make_response(str(prediction))
    response.mimetype = 'text/plain'
    return response

# Route pour prédire le sentiment
@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.json['text']
    result = distilled_student_sentiment_classifier(text)
    negative_score = [item['score'] for item in result[0] if item['label'] == 'negative'][0]
    return '1' if negative_score >= 0.5 else '0'

def run_toxicity_api():
    app.run(port=5000, debug=False)

def run_sentiment_api():
    app.run(port=5001, debug=False)

def main():
    # Lancer les deux processus en parallèle
    p1 = Process(target=run_toxicity_api)
    p2 = Process(target=run_sentiment_api)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()
