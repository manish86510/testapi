# Generated by Django 2.2.7 on 2019-11-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0007_auto_20191115_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myinterest',
            name='interact_code',
            field=models.CharField(max_length=200),
        ),
    ]