# Generated by Django 4.2.16 on 2025-03-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_num',
            field=models.CharField(max_length=11),
        ),
    ]
