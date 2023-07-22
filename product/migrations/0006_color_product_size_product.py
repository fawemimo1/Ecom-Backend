# Generated by Django 4.1.5 on 2023-07-22 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_color_remove_product_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='product.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='product.product'),
            preserve_default=False,
        ),
    ]