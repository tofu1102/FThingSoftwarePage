# Generated by Django 5.1.1 on 2024-09-21 02:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warikan', '0002_payment_ammount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to=settings.AUTH_USER_MODEL),
        ),
    ]
