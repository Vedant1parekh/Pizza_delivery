# Generated by Django 3.1.7 on 2021-07-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='orderstatus',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
