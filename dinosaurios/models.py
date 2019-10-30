from django.db import models

class Periodo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    

class Dinosaurio(models.Model):
    nombre = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    periodo = models.ForeignKey(Periodo, verbose_name="Periodo", 
        on_delete=models.CASCADE)
    imagen = models.ImageField("Imágen", upload_to='dinos',null=True, blank=True)

    def __str__(self):
        return self.nombre