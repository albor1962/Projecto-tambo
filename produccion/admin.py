from django.contrib import admin
from .models import DatosProductivos,IngresoAlimentos


class DatosProductivosAdmin(admin.ModelAdmin):
    list_display = ('fecha','vo','vpp','vs','vt','vaq_p','lts_venta','lts_consumo','litros_totales','litros_vo')

class IngresoAlimentosAdmin(admin.ModelAdmin):
    list_display = ('fecha','tipo','nombre','cant','precio_unit')

admin.site.register(DatosProductivos,DatosProductivosAdmin)
admin.site.register(IngresoAlimentos,IngresoAlimentosAdmin)
