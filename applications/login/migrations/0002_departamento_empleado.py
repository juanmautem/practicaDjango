# Generated by Django 4.1.3 on 2022-11-17 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=20, unique=True, verbose_name='Nombre corto')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=120, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('0', 'CONTABLE'), ('1', 'GERENTE'), ('2', 'ADMINISTRATIVO'), ('3', 'RECURSOS HUMANOS'), ('4', 'OTROS')], max_length=1, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.departamento')),
            ],
        ),
    ]