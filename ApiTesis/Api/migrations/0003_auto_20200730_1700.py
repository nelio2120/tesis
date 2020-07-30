# Generated by Django 2.2.5 on 2020-07-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_contacto_confian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_usuario',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='historial_usuario',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]