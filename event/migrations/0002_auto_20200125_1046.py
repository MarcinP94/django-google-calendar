# Generated by Django 3.0.2 on 2020-01-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='end',
            field=models.DateTimeField(null=True, verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start',
            field=models.DateTimeField(null=True, verbose_name='Start date'),
        ),
    ]
