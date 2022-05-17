# Generated by Django 4.0.4 on 2022-05-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.AddField(
            model_name='account',
            name='exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]