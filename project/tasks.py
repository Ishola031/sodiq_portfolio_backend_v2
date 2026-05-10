from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


@shared_task
def send_contact_email(number, firstName, lastName, user_email, message):
    html_content = render_to_string(
        "email/verify_email.html",
        {
            "number": number,
            "firstName": firstName,
            "lastName": lastName,
            "email": user_email,
            "message": message,
        }
    )

    user_html_content = render_to_string(
        "email/user_email.html",
        {
            "firstName": firstName,
        }
    )

    email_message = EmailMultiAlternatives(
        subject=f"Portfolio Contact: {firstName} {lastName}",
        body="New contact message",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["sannisodiq031@gmail.com"],
    )
    user_email_message = EmailMultiAlternatives(
        subject="Thanks for contacting me!",
        body="Thanks for reaching out.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user_email],
    )

    email_message.attach_alternative(html_content, "text/html")
    user_email_message.attach_alternative(user_html_content, "text/html")
    email_message.send(fail_silently=False)
    user_email_message.send(fail_silently=False)