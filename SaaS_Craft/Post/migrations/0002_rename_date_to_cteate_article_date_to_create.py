# Generated by Django 5.0.2 on 2024-02-24 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date_to_cteate',
            new_name='date_to_create',
        ),
    ]
