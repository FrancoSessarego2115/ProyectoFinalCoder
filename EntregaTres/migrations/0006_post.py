# Generated by Django 4.1.7 on 2023-04-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EntregaTres', '0005_tareas_delete_tarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_caption_title', models.CharField(max_length=30)),
                ('carousel_caption_description', models.CharField(max_length=80)),
                ('heading', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
    ]
