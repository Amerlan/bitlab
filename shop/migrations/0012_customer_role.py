# Generated by Django 3.2.9 on 2021-11-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='role',
            field=models.CharField(default='CLIENT', max_length=50),
        ),
    ]
