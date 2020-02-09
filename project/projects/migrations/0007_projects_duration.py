# Generated by Django 3.0.3 on 2020-02-08 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200209_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='duration',
            field=models.CharField(choices=[('1', '1 month'), ('2', '2 months'), ('3', '3 months'), ('4', '5 months'), ('6', '6 months'), ('7', '>6 months')], default='6', max_length=20),
        ),
    ]
