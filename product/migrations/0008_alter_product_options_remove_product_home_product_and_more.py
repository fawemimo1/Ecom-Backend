# Generated by Django 4.1.5 on 2023-07-25 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='home_product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_stock',
        ),
    ]