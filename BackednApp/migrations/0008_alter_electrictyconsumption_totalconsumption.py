# Generated by Django 4.0.4 on 2022-11-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackednApp', '0007_electrictyconsumption_totalconsumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electrictyconsumption',
            name='totalconsumption',
            field=models.IntegerField(),
        ),
    ]
