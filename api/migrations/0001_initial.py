# Generated by Django 4.2.6 on 2023-11-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('uname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('pass1', models.CharField(max_length=50)),
                ('pass2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Respuestaschatbot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_temporal', models.DateTimeField()),
                ('nombre_completo', models.CharField(max_length=100)),
                ('pregunta1', models.CharField(max_length=100)),
                ('pregunta2', models.TextField()),
                ('pregunta3', models.CharField(max_length=100)),
                ('pregunta4', models.TextField()),
                ('pregunta5', models.TextField()),
                ('pregunta6', models.CharField(max_length=100)),
                ('pregunta7', models.CharField(max_length=100)),
            ],
        ),
    ]
