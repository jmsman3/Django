# Generated by Django 5.0.6 on 2024-07-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_categorymodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Category/media/uploads/'),
        ),
    ]
