# Generated by Django 4.1.1 on 2022-09-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountTpm', '0011_accountexpenses_papersheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountexpenses',
            name='Toner',
            field=models.IntegerField(default=0),
        ),
    ]