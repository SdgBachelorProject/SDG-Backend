# Generated by Django 4.0.4 on 2022-12-13 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackednApp', '0009_alter_user_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='user',
        ),
    ]
