# Generated by Django 4.1.5 on 2023-07-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0010_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]