# Generated by Django 5.1.1 on 2024-09-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warikan', '0005_event_registration_stopped'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='receipt_image',
            field=models.ImageField(blank=True, upload_to='images/receipt/'),
        ),
    ]