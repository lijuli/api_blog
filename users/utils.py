import random
import string
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta


def get_random_code(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def send_mail_to_user(email, confirmation_code):
    send_mail(
        subject='Регистрация на Yamdb',
        message=f'Код подтверждения: {confirmation_code}',
        from_email='yamdb@gmail.com',
        recipient_list=[email],
        fail_silently=False,
    )


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token
    access_token.set_exp(lifetime=timedelta(days=30))

    return {
        #'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
