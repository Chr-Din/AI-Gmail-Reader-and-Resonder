import sqlite3
import os
from datetime import datetime

def init_db():
    os.makedirs("logs",exist_ok=True)
    conn = sqlite3.connect("logs/emails.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS email_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_id TEXT,
            subject TEXT,
            intent TEXT,
            response TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_email(email_id, subject, intent, reply_text):
    conn = sqlite3.connect("logs/emails.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO email_logs (email_id, subject, intent, response, timestamp) VALUES (?, ?, ?, ?, ?)",
                   (email_id, subject, intent, reply_text, datetime.now().isoformat()))
    conn.commit()
    conn.close()
