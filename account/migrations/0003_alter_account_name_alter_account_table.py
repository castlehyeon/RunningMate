# Generated by Django 4.0.4 on 2022-05-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_account_email_remove_account_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterModelTable(
            name='account',
            table='accounts',
        ),
    ]