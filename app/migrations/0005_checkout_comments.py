# Generated by Django 4.2.5 on 2023-10-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='comments',
            field=models.CharField(default='', max_length=50),
        ),
    ]
