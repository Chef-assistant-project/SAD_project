# Generated by Django 3.0.5 on 2020-07-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200730_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlike',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
