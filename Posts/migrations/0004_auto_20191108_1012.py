# Generated by Django 2.2.2 on 2019-11-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_auto_20191108_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='postcomments',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='postlikes',
            old_name='user_id',
            new_name='user',
        ),
    ]
