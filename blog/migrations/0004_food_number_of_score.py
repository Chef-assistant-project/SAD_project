# Generated by Django 3.0.5 on 2020-07-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200702_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='number_of_score',
            field=models.IntegerField(default=0),
        ),
    ]
