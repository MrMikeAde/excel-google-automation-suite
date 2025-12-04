import yagmail

def send_report(to_email, subject, body, attachments=None):
    yag = yagmail.SMTP("you@gmail.com","password")
    yag.send(to=to_email, subject=subject, contents=body, attachments=attachments)
