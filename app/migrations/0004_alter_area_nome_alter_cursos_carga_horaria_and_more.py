# Generated by Django 5.0.3 on 2024-04-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tipodeavaliacao_disciplinasporcursos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Área de Saber'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='carga_horaria',
            field=models.CharField(verbose_name='Carga horária do curso'),
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='telefone',
            field=models.CharField(verbose_name='Telefone da instituição'),
        ),
    ]
