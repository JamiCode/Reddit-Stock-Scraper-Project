# Generated by Django 3.1.7 on 2021-03-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedditStocksDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_ticker', models.TextField(max_length=5)),
                ('stock_mentions', models.IntegerField()),
            ],
        ),
    ]
