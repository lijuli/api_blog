from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from api_yamdb.settings import ADMIN_EMAIL, SUBJECT


def send_mail_to_user(email, confirmation_code):
    send_mail(
        subject=SUBJECT,
        message=f'Код подтверждения: {confirmation_code}',
        from_email=ADMIN_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token

    return {
        'access': str(access_token),
    }
