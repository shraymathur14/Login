# Generated by Django 4.1.7 on 2023-06-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_signin_pass1_remove_signup_pass1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='mail',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]