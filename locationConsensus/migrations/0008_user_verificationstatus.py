# Generated by Django 4.1.5 on 2023-02-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationConsensus', '0007_remove_user_verificationstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verificationStatus',
            field=models.CharField(default='False', max_length=20),
        ),
    ]
