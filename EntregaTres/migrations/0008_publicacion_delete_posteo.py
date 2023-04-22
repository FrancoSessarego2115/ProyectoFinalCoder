# Generated by Django 4.1.7 on 2023-04-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EntregaTres', '0007_posteo_delete_alumnos_delete_post_delete_profesores_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=30)),
                ('Categoria', models.CharField(max_length=80)),
                ('Descripccion_Posteo', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Posteo',
        ),
    ]