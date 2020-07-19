# Generated by Django 3.0.4 on 2020-07-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200702_1006'),
        ('users', '0006_auto_20200719_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='food',
        ),
        migrations.AddField(
            model_name='favorite',
            name='food',
            field=models.ManyToManyField(to='blog.Food'),
        ),
    ]
