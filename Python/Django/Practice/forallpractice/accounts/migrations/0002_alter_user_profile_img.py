# Generated by Django 3.2.13 on 2022-10-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='no_profile_pic.png', upload_to='image/profile_pic'),
        ),
    ]
