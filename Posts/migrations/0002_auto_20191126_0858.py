# Generated by Django 2.2.7 on 2019-11-26 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmedia',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_media', to='Posts.Post'),
        ),
    ]
