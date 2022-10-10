# Generated by Django 4.1.1 on 2022-09-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('BlackCopies', models.IntegerField()),
                ('ColourCopies', models.IntegerField()),
                ('B2bCopies', models.IntegerField()),
                ('PaperPresentToday', models.IntegerField()),
                ('PaperYesterday', models.IntegerField()),
                ('PaperSoldToday', models.IntegerField()),
                ('Bindings', models.IntegerField()),
                ('Expenses', models.IntegerField()),
                ('StayingCopies', models.IntegerField()),
                ('StayingMoney', models.IntegerField()),
                ('GoneCopiesPast', models.IntegerField()),
                ('GoneMoneyPast', models.IntegerField()),
                ('NotesToday', models.CharField(max_length=200)),
                ('CashIncome', models.IntegerField()),
                ('PaytmIncome', models.IntegerField()),
                ('TotalIncome', models.IntegerField()),
                ('OpeningBalance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LabourExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('TajPresent', models.IntegerField()),
                ('TajExpense', models.IntegerField()),
                ('NoorPresent', models.IntegerField()),
                ('NoorExpense', models.IntegerField()),
            ],
        ),
    ]