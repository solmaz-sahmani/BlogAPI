from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_welcome_email(user_email):
    send_mail(
        subject = "Wellcome to BlogAPI",
        message = "Your submit was seccessful",
        from_email= "solmaz.sahmani@gmail.com",
        recipient_list= [user_email],
    )