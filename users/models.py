from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from .utils import get_random_code


class CHOICES(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, username):
        user = self.create_user(
            email,
            password=password,
            username=username,
            role=CHOICES.MODERATOR,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            role=CHOICES.ADMIN,
        )
        user.staff = True
        user.superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20, unique=True, blank=False, null=False
    )
    password = models.CharField(max_length=128, blank=True, null=True)
    bio = models.TextField(
        max_length=1000, null=True, blank=True, verbose_name='Рассказ о себе'
    )
    role = models.CharField(
        max_length=15,
        choices=CHOICES.choices,
        default=CHOICES.USER,
        verbose_name='Роль',
    )
    email = models.EmailField(
        max_length=255, unique=True, blank=False, null=False
    )
    confirmation_code = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        default=get_random_code(10),
        verbose_name='Код подтверждения',
    )

    is_active = True

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', )

    ordering = ('-pk',)

    @property
    def is_superuser(self):
        return self.role == CHOICES.ADMIN

    @property
    def is_staff(self):
        return self.role == CHOICES.MODERATOR

    class Meta(AbstractUser.Meta):
        db_table = 'users_customuser'
        app_label = 'users'
        verbose_name = 'customuser'
        ordering = ('-pk',)
