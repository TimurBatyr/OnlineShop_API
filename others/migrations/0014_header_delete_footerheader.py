# Generated by Django 4.0.1 on 2022-04-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0013_rename_footer_image_footerheader_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Number', 'Number'), ('Email', 'Email'), ('Instagram', 'Instagram'), ('Telegram', 'Telegram'), ('WhatsApp', 'Whatsapp')], max_length=100)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='FooterHeader',
        ),
    ]
