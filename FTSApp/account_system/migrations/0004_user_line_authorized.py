# Generated by Django 5.1.1 on 2024-09-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_system', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='line_authorized',
            field=models.BooleanField(default=False),
        ),
    ]
