# Generated by Django 4.1.5 on 2023-08-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_payment_order_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]