# Generated by Django 5.1.1 on 2024-09-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinWarning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('condition', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('last_notified_price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Coin',
        ),
    ]
