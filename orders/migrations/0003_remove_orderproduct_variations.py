# Generated by Django 4.2 on 2023-04-07 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_id_alter_orderproduct_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variations',
        ),
    ]
