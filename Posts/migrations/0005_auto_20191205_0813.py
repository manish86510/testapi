# Generated by Django 2.2.7 on 2019-12-05 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_auto_20191203_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmedia',
            name='post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_media', to='Posts.Post'),
        ),
    ]