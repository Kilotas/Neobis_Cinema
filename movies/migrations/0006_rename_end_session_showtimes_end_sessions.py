# Generated by Django 4.2.9 on 2024-02-09 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_cinema_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showtimes',
            old_name='end_session',
            new_name='end_sessions',
        ),
    ]