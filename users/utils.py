import random
import string
from django.core.mail import send_mail

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
