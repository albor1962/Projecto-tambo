from django.urls import path, include
from produccion.views import RegistroCrear,RegistroList,DatosProductivosUpdate,DatosProductivosDelete, \
    ExistenciaList,ProLecheList,IngresoAlimentos_list



urlpatterns = [
    path('registro_list/', RegistroList.as_view(), name='registro_list'),
    path('registro_crear/', RegistroCrear.as_view(), name='registro_crear'),
    path('registro_editar/<int:pk>/', DatosProductivosUpdate.as_view(), name='registro_editar'),
    path('registro_eliminar/<int:pk>/', DatosProductivosDelete.as_view(), name='registro_eliminar'),

    path('existencia_list/', ExistenciaList.as_view(), name='existencia_list'),
    path('leche_list/', ProLecheList.as_view(), name='leche_list'),

    path('ingreso_alimentos_list/', IngresoAlimentos_list.as_view(), name='ingreso_alimentos_list'),

]