from django.db import models
from datetime import datetime
# Create your models here.
ESTADO = [
    ('A','ACTIVO')
    ,('I','INACTIVO')
]
class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,blank=True,null=True)
    apellido = models.CharField(max_length=50,blank=True,null=True)
    cedula = models.CharField(max_length=50,blank=True,null=True)
    fecha_nacimiento = models.DateField(max_length=45,blank=True,null=True)
    estado = models.CharField(max_length=50,blank=True,choices=ESTADO,default='A')

    class Meta:
        verbose_name = 'Persona'
        db_table = 'mant_persona'
    def __str__(self):
        return self.nombre
class Roles(models.Model):
    nombre = models.CharField(max_length=50,blank=True,null=True)
    estado = models.CharField(max_length=50,blank=True,choices=ESTADO,default='A')
    class Meta:
        verbose_name = 'Rol'
        db_table = "conf_rol"
    def __str__(self):
        return self.nombre
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,blank=True,unique=True)
    correo = models.CharField(max_length=50,blank=True,unique=True)
    password = models.CharField(max_length=50,blank=True)
    idPersona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    idRol = models.ForeignKey(Roles,on_delete=models.CASCADE,default=1)
    estado = models.CharField(max_length=50,blank=True,choices=ESTADO,default='A')

    class Meta:
        verbose_name = 'Usuario'
        db_table = 'conf_usuario'
        
    def __str__(self):
        return self.nombre



class Historial_Usuario(models.Model):
    idHistoUsuario = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="hist_usuario")
    lat = models.DecimalField(blank=True,null=True,max_digits=9, decimal_places=6)
    lon = models.DecimalField(blank=True,null=True,max_digits=9, decimal_places=6)
    fecha = models.DateTimeField(default=datetime.utcnow)
    estado = models.CharField(max_length=50,blank=True,choices=ESTADO,default='A')

    class Meta:
        verbose_name = 'Historial_Usuario'
        db_table = 'hist_usuario'
    def __str__(self):
        return self.idUsuario.nombre

class Acceso_Usuario(models.Model):
    idUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="acc_usuario")
    idHistoUsuario = models.ManyToManyField(Historial_Usuario,db_table='detalle_historico_acceso')

    class Meta:
        verbose_name = 'Acceso_Usuario'
        db_table = 'conf_acceso'
    def __str__(self):
        return self.idUsuario.nombre

class Contacto_confian(models.Model):
    idPersona = models.ManyToManyField(Persona,db_table='detalle_persona_confi')
    contacto_1 = models.CharField(max_length=50,blank=True)
    contacto_2 = models.CharField(max_length=50,blank=True)

    class Meta:
        verbose_name = 'Contacto_Confi'
        db_table = 'mant_persona_confian'
    def __str__(self):
        return self.idPersona.nombre
