# Generated by Django 5.0.6 on 2024-07-04 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='Relation',
        ),
    ]