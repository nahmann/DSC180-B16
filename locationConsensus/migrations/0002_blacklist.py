# Generated by Django 4.1.3 on 2023-02-07 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationConsensus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('userID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
