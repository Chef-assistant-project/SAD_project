# Generated by Django 3.0.5 on 2020-07-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('users', '0009_auto_20200719_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='food_likes',
            field=models.ManyToManyField(to='users.Food_likes'),
        ),
    ]
