# Generated by Django 4.1.7 on 2023-06-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('pass1', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('pass1', models.CharField(max_length=20)),
                ('pass2', models.CharField(max_length=20)),
            ],
        ),
    ]
