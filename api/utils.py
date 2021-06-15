import random
import string

from django.core.mail import send_mail

CONFIRMATION_CODE_LEN = 10


def send_mail_to_user(email, confirmation_code):
    send_mail(
        subject='Регистрация на Yamdb',
        message=f'Код подтверждения: {confirmation_code}',
        from_email='yamdb@gmail.com',
        recipient_list=[email],
        fail_silently=False,
    )
