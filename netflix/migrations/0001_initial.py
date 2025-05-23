# Generated by Django 5.2 on 2025-04-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('image', models.URLField()),
                ('duration', models.PositiveIntegerField(help_text='Duration in minutes')),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Sci-Fi', 'Sci-Fi'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Documentary', 'Documentary'), ('Animation', 'Animation')], max_length=20)),
            ],
        ),
    ]
