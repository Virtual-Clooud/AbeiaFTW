# Generated by Django 4.1.7 on 2023-05-03 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_alter_pedido_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cupom',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 14, 11, 39, 17326)),
        ),
    ]
