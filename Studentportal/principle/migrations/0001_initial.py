# Generated by Django 3.0.2 on 2020-04-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addcourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=50)),
                ('Course_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='addteacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_Name', models.CharField(max_length=50)),
                ('Teacher_Subjects', models.CharField(max_length=50)),
                ('Teacher_Subjects_Code', models.CharField(max_length=50)),
                ('Teacher_Username', models.CharField(max_length=50)),
                ('Teacher_Password', models.CharField(max_length=50)),
            ],
        ),
    ]
