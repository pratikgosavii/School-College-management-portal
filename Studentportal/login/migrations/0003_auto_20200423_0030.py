# Generated by Django 3.0.2 on 2020-04-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200422_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name_teacher', models.CharField(max_length=50)),
                ('password_teacher', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='login',
            new_name='login_principle',
        ),
    ]
