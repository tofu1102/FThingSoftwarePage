from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

