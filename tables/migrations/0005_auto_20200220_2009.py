# Generated by Django 3.0.3 on 2020-02-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_table_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='url',
            field=models.CharField(default='Unknown', max_length=2048),
        ),
    ]
