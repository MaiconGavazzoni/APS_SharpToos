# Generated by Django 2.2 on 2019-04-27 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.IntegerField(max_length=100, verbose_name='Código')),
                ('internal_description', models.CharField(blank=True, max_length=150, verbose_name='Descrição')),
                ('factory_name', models.CharField(blank=True, max_length=150, verbose_name='Nome de Fábrica')),
                ('manufacturer', models.CharField(blank=True, max_length=100, verbose_name='Fabricante')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Ferramenta',
                'verbose_name_plural': 'Ferramentas',
                'ordering': ['stock_code'],
            },
        ),
        migrations.CreateModel(
            name='Sharpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sharpen', models.CharField(max_length=100, verbose_name='Lista')),
                ('quantity', models.IntegerField(default=1, max_length=100, verbose_name='Quantidade')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('tools', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='sharp.Tools', verbose_name='Ferramenta')),
            ],
            options={
                'verbose_name': 'Lista',
                'verbose_name_plural': 'Listas',
                'ordering': ['-created'],
            },
        ),
    ]
