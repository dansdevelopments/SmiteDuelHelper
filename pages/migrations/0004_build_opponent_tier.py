# Generated by Django 2.2.4 on 2019-11-24 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20191124_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='opponent_tier',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]