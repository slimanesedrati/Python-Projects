# Generated by Django 4.0.2 on 2022-03-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='Car_pic'),
        ),
    ]
