import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Параметри для доступу до Gmail
email = "your_email@gmail.com"
password = "your_password"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Функція для відправки листа
def send_email(to_email, subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), _subtype="pdf")
            attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path)
            msg.attach(attachment)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Помилка при відправці листа: {e}")
        return False
    