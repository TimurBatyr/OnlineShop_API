# Generated by Django 4.0.1 on 2022-04-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0003_imagehelp_rename_image_imageaboutus_help'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='answer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
