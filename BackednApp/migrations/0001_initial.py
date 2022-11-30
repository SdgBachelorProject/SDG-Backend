# Generated by Django 4.0.4 on 2022-11-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('created', models.DateField()),
                ('signedIn', models.DateField()),
            ],
        ),
    ]
