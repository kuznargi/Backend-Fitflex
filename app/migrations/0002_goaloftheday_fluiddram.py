# Generated by Django 5.0.6 on 2024-05-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goaloftheday',
            name='fluidDram',
            field=models.CharField(choices=[('л', 'Литр'), ('мл', 'Миллилитр')], default='л', max_length=2),
        ),
    ]
