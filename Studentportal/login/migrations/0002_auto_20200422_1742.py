# Generated by Django 3.0.2 on 2020-04-22 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='usernmae_name_principle',
            new_name='user_name_principle',
        ),
    ]