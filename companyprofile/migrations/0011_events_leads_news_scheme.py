# Generated by Django 5.0.6 on 2024-05-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0010_alter_industry_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('banner', models.ImageField(upload_to='')),
                ('short_desc', models.CharField(max_length=250)),
                ('long_desc', models.CharField(max_length=2000)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('guests', models.CharField(max_length=250)),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('attachment', models.FileField(upload_to='')),
                ('status', models.TextField()),
                ('valid', models.BooleanField(default=True)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=250)),
                ('source', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250, unique=True)),
                ('short_desc', models.CharField(max_length=250)),
                ('long_desc', models.CharField(max_length=2000)),
                ('banner', models.ImageField(upload_to='')),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('url', models.CharField(max_length=300)),
                ('short_desc', models.CharField(max_length=250)),
                ('long_desc', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='')),
                ('launched_date', models.DateField()),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
    ]
