from django.db import models

# Create your models here.
#Super USer hardmode -> Hard12345

#Usuario de prueba test -> abc147852


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Fecha de Actualización")
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
    
    