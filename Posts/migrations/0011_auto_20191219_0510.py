# Generated by Django 2.2.7 on 2019-12-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0010_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='read_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
