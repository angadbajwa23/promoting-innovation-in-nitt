# Generated by Django 3.0.3 on 2020-02-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200208_1749'),
        ('users', '0002_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='projects',
            field=models.ManyToManyField(to='projects.projects'),
        ),
    ]