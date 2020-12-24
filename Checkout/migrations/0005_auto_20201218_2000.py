# Generated by Django 3.1.3 on 2020-12-18 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('Shop', '0007_product_detail'),
        ('Checkout', '0004_remove_order_shippeddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_product',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='Checkout.order'),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='Shop.product'),
        ),
    ]
