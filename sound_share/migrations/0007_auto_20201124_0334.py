# Generated by Django 3.1.3 on 2020-11-24 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sound_share', '0006_sound_pack_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='pack_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sound_share.pack'),
        ),
    ]
