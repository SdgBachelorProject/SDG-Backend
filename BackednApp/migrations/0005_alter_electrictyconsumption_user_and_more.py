# Generated by Django 4.1.3 on 2022-12-09 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackednApp', '0004_waterconsumption_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electrictyconsumption',
            name='user',
            field=models.OneToOneField(default='test', on_delete=django.db.models.deletion.CASCADE, to='BackednApp.user'),
        ),
        migrations.AlterField(
            model_name='heatingconsumption',
            name='user',
            field=models.OneToOneField(default='test', on_delete=django.db.models.deletion.CASCADE, to='BackednApp.user'),
        ),
        migrations.AlterField(
            model_name='waterconsumption',
            name='user',
            field=models.OneToOneField(default='test', on_delete=django.db.models.deletion.CASCADE, to='BackednApp.user'),
        ),
    ]
