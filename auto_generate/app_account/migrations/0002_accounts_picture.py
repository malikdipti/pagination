# Generated by Django 2.2.4 on 2019-10-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='picture',
            field=models.ImageField(default=False, upload_to='acc_images'),
        ),
    ]
