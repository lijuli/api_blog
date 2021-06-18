
from django.db import models

from django.db import models
class qwerty(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'

print(qwerty.ADMIN)