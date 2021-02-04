from django import forms
from .models import DatosProductivos

class DatosProductivosForm(forms.ModelForm):
    class Meta:
        model = DatosProductivos
        fields = ['fecha','vo','vpp','vs','vaq_p','vaq_crec','toros','terneros','lts_venta','lts_consumo']
        labels = {'fecha':'Fecha','vo':'Vacas en ordene','vpp':'Vacas en pre parto','vs':'Vacas secas','vaq_p':'Vaquillonas prenadas','vaq_crec':'Vaquillonas en crecimiento',\
            'toros':'Toros','terneros':'Terneros','lts_venta':'Lts. vendidos','lts_consumo':'Lts. terneros'}
        widgets = {
            'fecha': forms.DateInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese fecha del registro',
                }
            ),
            'vo': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Vacas en ordene',
                }
            ),
            'vpp': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Vacas en pre-parto',
                }
            ),
            'vs': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Vacas secas',
                }
            ),
            'vaq_p': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Vaquillonas prenadas',
                }
            ),
            'vaq_crec': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Vaquillonas en crecimiento',
                }
            ),
            'toros': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Toros',
                }
            ),
            'terneros': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Terneros',
                }
            ),
            'lts_venta': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese litros vendidos',
                }
            ),
            'lts_consumo': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese litros a terneros',
                }
            ),
        }

# class ProLecheForm(forms.ModelForm):
#     model = DatosProductivos
#     fields = ['lts_venta','lts_consumo']
#     labels = {'lts_venta':'Lts.vendidos','lts_consumo':'Lts.consumo'}
#     widgets = {
#             'lts_venta': forms.TextInput(
#                 attrs = {
#                     'class':'form-control',
#                     'placeholder':'Ingrese litros vendidos',
#                 }
#             ),
#             'lts_consumo': forms.TextInput(
#                 attrs = {
#                     'class':'form-control',
#                     'placeholder':'Ingrese litros a terneros',
#                 }
#             ),

#     }