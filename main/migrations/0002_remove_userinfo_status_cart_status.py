# Generated by Django 4.0.1 on 2022-04-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='status',
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Ordered', 'Ordered'), ('Canceled', 'Canceled')], default=('New', 'New'), max_length=50),
        ),
    ]
