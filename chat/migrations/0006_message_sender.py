# Generated by Django 4.2.6 on 2023-10-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_message_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=255),
        ),
    ]
