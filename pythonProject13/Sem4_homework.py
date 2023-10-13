import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pytest
from logging_config import setup_logging


def send_test_report_via_email(report_file):
    email_address = 'your_email@gmail.com'
    email_password = 'your_password'
    recipient_email = 'recipient_email@example.com'

    subject = 'Отчет о тестах pytest'
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = recipient_email
    message['Subject'] = subject

    body = "Отчет о тестах pytest во вложении."
    message.attach(MIMEText(body, 'plain'))

    with open(report_file, 'rb') as attachment:
        part = MIMEText(attachment.read(), 'base64')
        part.add_header('Content-Disposition', f'attachment; filename="{report_file}"')
        message.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)

    server.sendmail(email_address, recipient_email, message.as_string())

    server.quit()


if __name__ == '__main__':
    logger = setup_logging()

    pytest.main(['-v', '--html=pytest_report.html'])

    send_test_report_via_email('pytest_report.html')