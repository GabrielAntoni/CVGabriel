# Generated by Django 5.0.4 on 2024-04-26 18:54

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nomeCert', models.CharField(max_length=100, verbose_name='Nome do Certificado')),
                ('dataCert', models.DateField(verbose_name='Data de Conclusão')),
                ('LinkCert', models.CharField(max_length=100, verbose_name='Link do Certificado')),
                ('duracaoCert', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Duração de Conclução do certificado')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='certificados', variations={'thumb': (124, 124)}, verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
            },
        ),
    ]