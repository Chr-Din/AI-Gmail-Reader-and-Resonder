# AI-Gmail-Reader-and-Resonder
This system automatically reads the unread mails ,classifies that as leave request, complaint or inquiry and replies to them accordingly
# AI Email Reader and Responder

This project is an automated AI-powered email reader and responder system built in Python. It reads unread Gmail messages, classifies them by intent using a transformer-based NLP model, sends a pre-defined reply accordingly, and logs the details in a local SQLite database.

---

## Features

* Automatically fetches unread Gmail messages.
* Classifies emails using a transformer model (`distilbert-base-uncased-finetuned-sst-2-english`).
* Sends contextual auto-responses based on detected intent (`leave`, `complaint`, `inquiry`, `general`).
* Logs email interactions for auditing and tracking.
* Simple setup with Flask, transformers, Gmail API, and SQLite.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-email-responder.git
cd ai-email-responder
```

### 2. Install Dependencies

Ensure you have Python 3.8+ installed. All required packages are listed in the `requirement.txt` file. To install them, run:

```bash
pip install -r requirement.txt
```

### 3. Set Up Gmail API Credentials

* Go to the [Google Cloud Console](https://console.cloud.google.com/).
* Create a project and enable the Gmail API.
* Generate OAuth 2.0 client credentials and download the `credentials.json` file.
* Place `credentials.json` in the project root directory.

### 4. Run the Script

```bash
python main.py
```

The script will open a browser window for you to authenticate with your Gmail account. It will then check for unread emails, classify them, send appropriate replies, and log each interaction.

---

## File Overview

* `main.py` – Entry point to initialize the app and process unread emails.
* `email_reader.py` – Connects to Gmail API, retrieves unread messages.
* `classifier.py` – Uses HuggingFace transformers to classify emails.
* `responder.py` – Generates and sends replies via Gmail API.
* `logger.py` – Logs processed emails into a SQLite database (`logs/emails.db`).
* `requirement.txt` – List of required Python packages.

---

## Example Reply Templates

The following intents are supported:

* **leave** → "Hi, your leave request has been received. We'll get back to you soon."
* **complaint** → "Hi, thank you for the feedback. We're reviewing your complaint."
* **inquiry** → "Hello, thank you for your inquiry. We'll respond shortly."
* **general** → "Thanks for reaching out. We will get back to you."

These can be modified in `responder.py`.

---

## Customization Tips

* **Model Fine-tuning**: For better classification, fine-tune `distilbert-base-uncased` on a domain-specific dataset.
* **Intent Mapping**: Customize intent labels and associated replies in `classifier.py` and `responder.py`.
* **Scheduling**: Use `schedule` or a cron job to run the script periodically.
