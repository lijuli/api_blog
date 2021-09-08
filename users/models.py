import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class Roles(models.TextChoices):
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
        )
        user.staff = True
        user.role = Roles.MODERATOR
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.staff = True
        user.superuser = True
        user.role = Roles.ADMIN
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )
    password = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )
    bio = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='About'
    )
    role = models.CharField(
        max_length=15,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name='Role',
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    confirmation_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    date_joined = models.DateTimeField(
        null=True,
        blank=True
    )
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', )

    ordering = ('-pk',)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_superuser(self):
        return self.role == Roles.ADMIN or self.superuser

    @property
    def is_staff(self):
        return self.role == Roles.MODERATOR or self.staff

    class Meta(AbstractUser.Meta):
        db_table = 'users_customuser'
        app_label = 'users'
        verbose_name = 'customuser'
        ordering = ('-pk',)
