# Generated by Django 3.2.7 on 2021-10-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20211015_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=0.5),
        ),
    ]
