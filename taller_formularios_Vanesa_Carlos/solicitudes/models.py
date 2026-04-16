from django.db import models


class Solicitud(models.Model):
    ACADEMICA = 'academica'
    ADMINISTRATIVA = 'administrativa'
    TECNICA = 'tecnica'
    OTRA = 'otra'

    TIPOS_SOLICITUD = [
        (ACADEMICA, 'Académica'),
        (ADMINISTRATIVA, 'Administrativa'),
        (TECNICA, 'Técnica'),
        (OTRA, 'Otra'),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=30)
    correo_electronico = models.EmailField()
    telefono_contacto = models.PositiveBigIntegerField()
    tipo_solicitud = models.CharField(max_length=20, choices=TIPOS_SOLICITUD)
    asunto = models.CharField(max_length=150)
    descripcion_detallada = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to='solicitudes/', blank=True, null=True)

    def __str__(self):
        return f'{self.asunto} - {self.nombre_solicitante}'
