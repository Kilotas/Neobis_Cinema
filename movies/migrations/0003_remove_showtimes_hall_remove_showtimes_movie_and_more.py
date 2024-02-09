# Generated by Django 4.2.9 on 2024-02-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_showtimes_hall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtimes',
            name='hall',
        ),
        migrations.RemoveField(
            model_name='showtimes',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='date_end',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='movie',
            name='date_start',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='movieformat',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]