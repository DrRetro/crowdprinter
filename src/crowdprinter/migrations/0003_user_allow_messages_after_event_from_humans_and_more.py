# Generated by Django 5.1.4 on 2024-12-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crowdprinter", "0002_user_max_attempts"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="allow_messages_after_event_from_humans",
            field=models.BooleanField(
                default=None,
                help_text="Das c3tactile Team darf dich per E-Mail für über zukünftige Events informieren",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="allow_messages_during_event_from_humans",
            field=models.BooleanField(
                default=None,
                help_text="Das c3tactile Team darf dich *während* dem Event kontaktieren",
                null=True,
            ),
        ),
    ]