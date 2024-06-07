# Generated by Django 5.0.6 on 2024-06-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='banner',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='company_banners/'),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='path/to/default/logo.jpg', upload_to='company_logos/'),
        ),
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
