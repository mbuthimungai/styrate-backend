from celery import shared_task
from smtplib import SMTP, SMTP_PORT
from pydantic import EmailStr
from app.core.settings import settings
import ssl
import os

context = ssl.create_default_context()
@shared_task(bind=True, autoretry_for=(Exception, ), retry_backoff=True,
             retry_kwargs={"max_retries": 5}, name="send_email:send_email")
def send_email(self, to_address: EmailStr, msg: str):
    with SMTP(host=settings.SMTP_HOST, port=settings.SMTP_PORT) as smtp:
        smtp.starttls(context=context)
        smtp.login(user=settings.EMAILS_FROM_EMAIL, password=settings.SMTP_PASSWORD)
        smtp.sendmail(from_addr=settings.EMAILS_FROM_EMAIL, to_addrs=to_address,
                      msg=msg)
    return {"status": "Email sent successfully!"}
        