# Generated by Django 4.2.7 on 2023-11-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('collge', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
            ],
        ),
    ]
