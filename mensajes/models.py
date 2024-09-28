from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fechaEnvio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'mensaje de {self.remitente} para {self.destinatario}: {self.contenido}'