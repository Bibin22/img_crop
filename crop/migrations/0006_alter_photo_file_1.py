# Generated by Django 3.2.6 on 2021-08-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0005_alter_photo_file_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]