# Generated by Django 4.1.5 on 2023-07-25 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-date_created']},
        ),
    ]
