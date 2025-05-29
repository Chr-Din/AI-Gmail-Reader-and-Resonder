from transformers import pipeline

# Load lightweight classifier
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
def classify_email(text):
    result = classifier(text[:512])[0]  # Truncate to 512 tokens
    label = result['label'].lower()
    if "leave" in text.lower():
        return "leave"
    elif "complaint" in text.lower() or "issue" in text.lower():
        return "complaint"
    elif "inquiry" in text.lower() or "question" in text.lower():
        return "inquiry"
    else:
        return "general"
