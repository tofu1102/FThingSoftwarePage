# Generated by Django 5.1.1 on 2024-09-20 10:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_system', '0004_user_line_authorized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]