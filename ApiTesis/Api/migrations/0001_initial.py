# Generated by Django 2.2.5 on 2020-08-14 01:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idPersona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('cedula', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, max_length=45, null=True)),
                ('estado', models.CharField(blank=True, choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=50)),
            ],
            options={
                'verbose_name': 'Persona',
                'db_table': 'mant_persona',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, unique=True)),
                ('correo', models.CharField(blank=True, max_length=50, unique=True)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('estado', models.CharField(blank=True, choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=50)),
                ('idPersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Persona')),
            ],
            options={
                'verbose_name': 'Usuario',
                'db_table': 'conf_usuario',
            },
        ),
        migrations.CreateModel(
            name='Historial_Usuario',
            fields=[
                ('idHistoUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('estado', models.CharField(blank=True, choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=50)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hist_usuario', to='Api.Usuario')),
            ],
            options={
                'verbose_name': 'Historial_Usuario',
                'db_table': 'hist_usuario',
            },
        ),
        migrations.CreateModel(
            name='Contacto_confian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacto_1', models.CharField(blank=True, max_length=50)),
                ('contacto_2', models.CharField(blank=True, max_length=50)),
                ('idPersona', models.ManyToManyField(db_table='detalle_persona_confi', to='Api.Persona')),
                ('idUsuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='id_usuario_confianza', to='Api.Usuario')),
            ],
            options={
                'verbose_name': 'Contacto_Confi',
                'db_table': 'mant_persona_confian',
            },
        ),
        migrations.CreateModel(
            name='Acceso_Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idHistoUsuario', models.ManyToManyField(db_table='detalle_historico_acceso', to='Api.Historial_Usuario')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acc_usuario', to='Api.Usuario')),
            ],
            options={
                'verbose_name': 'Acceso_Usuario',
                'db_table': 'conf_acceso',
            },
        ),
    ]
