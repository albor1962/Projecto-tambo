class Existencia(models.Model):
    fecha = models.DateField()
    vo = models.IntegerField(verbose_name='Vacas en ordeno')
    vpp = models.IntegerField(verbose_name='Vacas Pre Parto')
    vs = models.IntegerField(verbose_name='Vacas Secas')
    vaq_pc = models.IntegerField(verbose_name='Vaquillonas prenadas')
    vaq_crecimiento = models.IntegerField(verbose_name='Vaquillonas en desarrollo')
    toros = models.IntegerField(verbose_name='Toros')
    terneros = models.IntegerField(verbose_name='Terneros en guachera')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Existencia'
        verbose_name_plural = 'Existencias'
        ordering = ['-fecha']

    def __str__(self):
        return str(self.fecha)
    
    def _get_vacas_total(self):
        return self.vo + self.vpp + self.vs
    vacas_totales = property(_get_vacas_total)


class ProLeche(models.Model):
    fecha = models.ForeignKey(Existencia, verbose_name='Fecha', on_delete=models.CASCADE)
    lts_venta = models.IntegerField(verbose_name='Litros vendidos')
    lts_terneros = models.IntegerField(verbose_name='Litros Terneros')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Produccion de leche'
        verbose_name_plural = 'Producciones de leche'
        ordering = ['-fecha']

    def get_lts_totales(self):
        return self.lts_venta + self.lts_terneros
    litros_totales = property(get_lts_totales)

    def get_ltsxvo(self):
        return self.litros_totales / self.existencia_vo
    litros_vo = property(get_ltsxvo)
    

    def __str__(self):
        return str(self.fecha)