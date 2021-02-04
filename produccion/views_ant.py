from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Existencia,ProLeche
from .forms import ExistenciaForm


class ExistenciaList(ListView):
    model = Existencia
    template_name: 'produccion/existencia_list.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    

class ExistenciaCrear(CreateView):
    model = Existencia
    form_class = ExistenciaForm
    template_name = 'produccion/existencia_crear.html'
    success_url = reverse_lazy('produccion:existencia_list')

class ExistenciaUpdate(UpdateView):
    model = Existencia
    form_class = ExistenciaForm
    template_name = 'produccion/existencia_crear.html'
    success_url = reverse_lazy('produccion:existencia_list')

class ExistenciaDelete(DeleteView):
    model = Existencia

    def post(self,request, pk,*args,**kwargs):
        object = Existencia.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('produccion:existencia_list')

class ProLecheList(ListView):
    model = ProLeche
    template_name: 'produccion/proleche_list.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)
