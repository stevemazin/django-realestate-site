# Generated by Django 2.2.13 on 2021-02-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210224_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='rental',
            field=models.BooleanField(default=False),
        ),
    ]