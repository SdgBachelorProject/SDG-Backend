# Generated by Django 4.0.4 on 2022-12-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackednApp', '0002_remove_heatingconsumption_electricityconsumptionperhour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electrictyconsumption',
            name='electricityConsumption',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
