# Generated by Django 2.2.14 on 2020-07-07 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200707_1030"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="test",),
    ]
