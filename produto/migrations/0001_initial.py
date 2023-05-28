# Generated by Django 4.1.7 on 2023-04-05 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('maximo', models.IntegerField()),
                ('minimo', models.IntegerField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Opcoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('acrecimo', models.FloatField(default=0)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='post_img')),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('ingredientes', models.CharField(max_length=2000)),
                ('ativo', models.BooleanField(default=True)),
                ('adicionais', models.ManyToManyField(blank=True, to='produto.adicional')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='adicional',
            name='opcoes',
            field=models.ManyToManyField(to='produto.opcoes'),
        ),
    ]
