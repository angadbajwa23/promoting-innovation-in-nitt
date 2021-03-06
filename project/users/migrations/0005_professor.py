# Generated by Django 3.0.3 on 2020-02-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200209_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your full name', max_length=200)),
                ('email', models.CharField(help_text='Enter your institute e-mail', max_length=200)),
                ('department', models.CharField(choices=[('CHEM', 'Chemical Engineering'), ('CSE', 'Computer Science and Engineering'), ('CIVIL', 'Civil Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('ECE', 'Electronics and Communications Engineering'), ('ICE', 'Instrumentation and Control Engineering'), ('MECH', 'Mechanical Engineering'), ('META', 'Metallurgical and Materials Engineering'), ('PROD', 'Production Engineering')], max_length=200)),
                ('research_areas', models.CharField(help_text='Enter comma separated Areas of research', max_length=200)),
                ('google_scholar', models.CharField(blank=True, help_text='Enter your Google scholar ID', max_length=200)),
            ],
        ),
    ]
