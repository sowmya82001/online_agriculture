# Generated by Django 5.0.6 on 2025-03-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='farmer',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='price_per_kg',
        ),
        migrations.AddField(
            model_name='crop',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='crop',
            name='type',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='farmer',
            name='location',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
