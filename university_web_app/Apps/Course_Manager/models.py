from django.db import models

# Create your models here.

class Estudiante(models.Model):

	Primer_Apellido = models.CharField(max_length = 35)
	Segundo_Apellido = models.CharField(max_length = 35)
	Nombres = models.CharField(max_length = 35)
	Cedula = models.CharField(max_length = 8)
	Fecha_Nacimiento = models.DateField()
	Sex_Ops = (('F', 'Femenino'), ('M', 'Masculino'))
	Genero = models.CharField(max_length = 1, choices = Sex_Ops, default = 'M')

	def NombreCompleto(self):
		return '{} {}, {}'.format(self.Primer_Apellido, self.Segundo_Apellido, self.Nombres)

	def __str__(self):
		return self.NombreCompleto()

class Curso(models.Model):

	Nombre = models.CharField(max_length = 50)
	Creditos = models.PositiveSmallIntegerField()
	Estado = models.BooleanField(default = True)

	def __str__(self):
		return '{} ({})'.format(self.Nombre, self.Creditos)

class Matricula(models.Model):

	Estudiante = models.ForeignKey(Estudiante, null = False, blank = False, on_delete = models.CASCADE)
	Curso = models.ForeignKey(Curso, null = False, blank = False, on_delete = models.CASCADE)
	Fecha_Matricula = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '{} => {}'.format(self.Estudiante, self.Curso.Nombre)
