# Generated by Django 5.1.1 on 2024-09-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_alert_timestamp_alter_session_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='datetime',
            field=models.DateTimeField(verbose_name='session date'),
        ),
    ]
