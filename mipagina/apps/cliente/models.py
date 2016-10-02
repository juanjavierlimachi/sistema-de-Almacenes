from django.db import models
# Create your models here.
class Trabajador(models.Model):
	Nombre_trabajador=models.CharField(max_length=150)
	Apellidos=models.CharField(max_length=150)
	Ci_Nit=models.PositiveIntegerField(max_length=8,unique=True)
	Telefono=models.PositiveIntegerField(max_length=15)
	Direccion=models.CharField(max_length=150)
	fecha_registro = models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		#return self.Nombre_trabajador
		return "%s %s Nit:%s"%(self.Nombre_trabajador,self.Apellidos,self.Ci_Nit)