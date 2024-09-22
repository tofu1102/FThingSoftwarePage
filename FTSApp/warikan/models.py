from django.db import models
from account_system.models import User
import uuid
from django.utils import timezone

class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(User)
    registration_stopped = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="images/thumbnail/", blank=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payer")
    payee = models.ManyToManyField(User, related_name="payee")
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=0)
    receipt_image = models.ImageField(upload_to="images/receipt/", blank=True)

    def __str__(self) -> str:
        return self.name


# Create your models here.
