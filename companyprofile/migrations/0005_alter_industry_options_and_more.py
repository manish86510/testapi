# Generated by Django 5.0.6 on 2024-06-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0004_delete_admin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='industry',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='company',
            old_name='isverify',
            new_name='is_verify',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='updted_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='company',
            new_name='company_id',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='image',
        ),
        migrations.AddField(
            model_name='scheme',
            name='banner',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='scheme_banners/'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='attachment',
            field=models.FileField(default='files_uploads/default.pdf', upload_to='files_uploads/'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
