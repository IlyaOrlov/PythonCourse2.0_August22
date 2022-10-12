from smtplib import SMTP_SSL
from email.mime.text import MIMEText


def send(message):
    sender = 'python.course@mail.ru'
    targets = ['orlov.soft.company@gmail.com']

    msg = MIMEText(message)
    msg['Subject'] = 'Simple subject'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    server = SMTP_SSL('smtp.mail.ru', 465)
    server.login(sender, 'CVul9R2wTuFbdgomGjGK')
    server.sendmail(sender, targets, msg.as_string())
    server.quit()


send("Привет2")
