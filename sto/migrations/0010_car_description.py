# Generated by Django 3.0.4 on 2020-03-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sto', '0009_remove_repair_repair_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.CharField(default='нет описания', max_length=10, verbose_name='описание'),
        ),
    ]
