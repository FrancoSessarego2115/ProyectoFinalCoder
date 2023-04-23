# Generated by Django 4.1.7 on 2023-04-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EntregaTres', '0015_mensajes'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='Categorias',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='Categoria',
            field=models.CharField(choices=[('Alienigenas', 'Alienigenas'), ('Reptilianos', 'Reptilianos'), ('Teorias', 'Teorias Conspirativas')], max_length=30),
        ),
    ]
