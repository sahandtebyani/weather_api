# Generated by Django 3.2 on 2021-04-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_description', models.IntegerField(choices=[(0, 'Sunny'), (1, 'Rain'), (2, 'Cloudy'), (3, 'Snow')], default=0)),
                ('temperature', models.FloatField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]