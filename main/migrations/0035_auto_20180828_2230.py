# Generated by Django 2.0.1 on 2018-08-28 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20180828_1400'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Opus',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='opusid',
        ),
    ]