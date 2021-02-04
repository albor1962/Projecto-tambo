from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import DatosProductivos,IngresoAlimentos
from .forms import DatosProductivosForm


class RegistroCrear(CreateView):
    model = DatosProductivos
    form_class = DatosProductivosForm
    template_name = 'produccion/registro_crear.html'
    success_url = reverse_lazy('produccion:registro_list')


class RegistroList(ListView):
    model = DatosProductivos
    template_name = 'produccion/registro_list.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)


class DatosProductivosUpdate(UpdateView):
    model = DatosProductivos
    form_class = DatosProductivosForm
    template_name = 'produccion/registro_crear.html'
    success_url = reverse_lazy('produccion:registro_list')

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

class DatosProductivosDelete(DeleteView):
    model = DatosProductivos
    template_name = 'produccion/registro_confirm_delete.html'

    def post(self,request, pk,*args,**kwargs):
        object = DatosProductivos.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('produccion:registro_list')


class ProLecheList(ListView):
    model = DatosProductivos
    template_name = 'produccion/proLeche_list.html'
    # form_class = ProLecheForm

    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    

class ExistenciaList(ListView):
    model = DatosProductivos
    template_name = 'produccion/existencia_list.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)


class IngresoAlimentos_list(ListView):
    model = IngresoAlimentos
    template_name = 'produccion/ingresoAlimentos_list.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)
        