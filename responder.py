import base64
reply_templates = {
    'leave': "Hi, your leave request has been received. We'll get back to you soon.",
    'complaint': "Hi, thank you for the feedback. We're reviewing your complaint.",
    'inquiry': "Hello, thank you for your inquiry. We'll respond shortly.",
    'general': "Thanks for reaching out. We will get back to you."
}
def generate_reply(intent, sender_name):
    display_name = sender_name.split('<')[0].strip()
    body = reply_templates.get(intent, reply_templates['general'])
    closing = "\n\nWith regards,\nmailguyharry@gmail.com"
    return f"Dear {display_name},\n\n{body}{closing}"
def send_reply(service, email, reply_text):
    # Construct the raw email message
    message = {
        'raw': base64.urlsafe_b64encode(
            f"To: {email['sender']}\r\n"
            f"Subject: Re: {email['subject']}\r\n\r\n"
            f"{reply_text}".encode("utf-8")
        ).decode("utf-8")
    }
    # Send the reply
    service.users().messages().send(userId="me", body=message).execute()
    # Mark the original email as read
    service.users().messages().modify(
        userId='me',
        id=email['id'],
        body={'removeLabelIds': ['UNREAD']}
    ).execute()
