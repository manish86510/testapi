# Generated by Django 2.2.7 on 2019-11-21 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_auto_20191121_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='target_audience_interests',
            new_name='target_audience',
        ),
    ]
