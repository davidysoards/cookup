# Generated by Django 3.1.3 on 2020-12-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sound_share', '0010_auto_20201124_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='sound',
            name='tempo',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
