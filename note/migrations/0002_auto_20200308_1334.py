# Generated by Django 2.1.8 on 2020-03-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(height_field=60, upload_to='img', width_field=100),
        ),
    ]
