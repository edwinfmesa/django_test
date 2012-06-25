from django.db import models


class comentarios(models.Model):
    titulo = models.CharField(max_length = 20)
    fecha = models.DateTimeField()
    texto = models.TextField(blank = True)
    hola ="hola mundo" 
    
    def __unicode__(self):
        return "%s "%(self.titulo)

   
    
    
    
    
    
    