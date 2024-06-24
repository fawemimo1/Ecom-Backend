# Generated by Django 4.1.5 on 2023-09-21 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_categorytype_remove_category_type_delete_type_and_more'),
        ('product', '0002_homebannerimage_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.categorytype'),
        ),
    ]