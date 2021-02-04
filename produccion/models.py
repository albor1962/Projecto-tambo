from django.db import models

TIPO_ALIMENTO = [
    ('Cereales','Cereales'),
    ('ConcTamb','Concentrado tambo'),
    ('ConcTern','Concentrado terneros'),
    ('ConcRecr','Concentrado recria'),
    ('Rollos','Rollos'),
    ('Silo','Silo'),
]



class DatosProductivos(models.Model):
    fecha = models.DateField()
    vo = models.IntegerField(verbose_name='VO', blank=True, null=True)
    vpp = models.IntegerField(verbose_name='VPP', blank=True, null=True)
    vs = models.IntegerField(verbose_name='VS', blank=True, null=True)
    vaq_p = models.IntegerField(verbose_name='Vaq.P', blank=True, null=True)
    vaq_crec = models.IntegerField(verbose_name='Vaq.Crec', blank=True, null=True)
    toros = models.IntegerField(verbose_name='Toros', blank=True, null=True)
    terneros = models.IntegerField(verbose_name='Terneros', blank=True, null=True)
    lts_venta = models.IntegerField(verbose_name='Lts.vta', blank=True, null=True)
    lts_consumo = models.IntegerField(verbose_name='Lts.cons', blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Datos productivos'
        verbose_name_plural = 'Datos productivos'
        ordering = ['-fecha']
    
    def _get_vacas_total(self):
        return self.vo + self.vpp + self.vs
    vt = property(_get_vacas_total)

    def _get_lts_totales(self):
        return self.lts_venta + self.lts_consumo
    litros_totales = property(_get_lts_totales)

    def _get_lts_vo(self):
        return (self.lts_venta + self.lts_consumo) / int(self.vo)
    litros_vo = property(_get_lts_vo)

    def __str__(self):
        return str(self.fecha)


class IngresoAlimentos(models.Model):
    fecha = models.ForeignKey(DatosProductivos, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo de alimento', max_length=50, choices=TIPO_ALIMENTO)
    nombre = models.CharField('Nombre alimento', max_length=100)
    cant = models.IntegerField('Cantidad')
    precio_unit = models.IntegerField('Precio unitario')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Ingreso de alimentos'
        verbose_name_plural = 'Ingreso de alimentos'
        ordering = ['-fecha']
        
    def __str__(self):
        return str(self.fecha)