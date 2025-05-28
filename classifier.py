from transformers import pipeline
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
def classify_email(text):
    result = classifier(text[:512])[0]  # Truncate to 512 tokens
    label = result['label'].lower()
    if "leave" in label:
        return "leave"
    elif "complaint" in label:
        return "complaint"
    elif "inquiry" in label or "question" in label:
        return "inquiry"
    else:
        return "general"
