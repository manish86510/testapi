# Generated by Django 2.2.7 on 2019-12-13 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Posts', '0008_postmedia_media_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttag',
            name='tag_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_tag_user', to=settings.AUTH_USER_MODEL),
        ),
    ]