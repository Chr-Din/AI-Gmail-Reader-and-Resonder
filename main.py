from email_reader import get_gmail_service, get_unread_emails
from classifier import classify_email
from responder import generate_reply, send_reply
from logger import init_db, log_email

def main():
    init_db()
    service = get_gmail_service()
    emails = get_unread_emails(service)

    if not emails:
        print("No unread emails found.")
        return

    for email in emails:
        intent = classify_email(email['body'])
        reply = generate_reply(intent, email['sender'])
        send_reply(service, email, reply)
        log_email(email['id'], email['subject'], intent, reply)

if __name__ == "__main__":
    main()
