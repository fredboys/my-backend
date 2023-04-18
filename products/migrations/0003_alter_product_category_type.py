# Generated by Django 3.2.18 on 2023-04-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_type',
            field=models.CharField(choices=[('food', 'Food'), ('drink', 'Drink'), ('toys', 'Toys'), ('technology', 'Technology'), ('sports', 'Sports'), ('clothing', 'Clothing'), ('footwear', 'Footwear'), ('household', 'Household'), ('homeware', 'Homeware'), ('other', 'Other')], max_length=50),
        ),
    ]