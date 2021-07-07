from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . import models


class formColaborador(ModelForm):
    
    class Meta:
        model = models.Colaborador
        fields = ['rutColaborador','imgColaborador','nombreColaborador','telefColaborador','direccionColaborador','emailColaborador','paisColaborador','contraseñaColaborador']
        widgets = {
            'rutColaborador': forms.NumberInput(
                attrs={
                    'class':'',
                    'id':'rutColaborador',
                    'name':'rutColaborador'
                }
            ),
            'imgColaborador' : forms.ClearableFileInput(
                attrs={
                    'class':''    
                }
            ),
            'nombreColaborador': forms.TextInput(
                attrs={
                    'class':'',
                    'id':'nombreColaborador',
                    'name':'nombreColaborador',
                    'minlength':'8',
                }
            ),
            'telefColaborador': forms.NumberInput(
                attrs={
                    'class':'',
                    'id':'telefColaborador',
                    'name':'telefColaborador',
                    'minlength':'9'
                }
            ),
            'direccionColaborador': forms.TextInput(
                attrs={
                    'class':'',
                    'id':'direccionColaborador',
                    'name':'direccionColaborador',
                    'minlength':'20'
                }
            ),
            'emailProveedor': forms.TextInput(
                attrs={
                    'class':'',
                    'placeholder':'Ingrese su email',
                    'id':'emailProveedor',
                    'name':'emailProveedor',
                    'type': 'email',
                    'minlength':'25'
                }
            ),
            'paisColaborador':forms.TextInput(
                attrs={
                    'id':'paisColaborador'
                }
            ),
            'contraseñaColaborador': forms.TextInput(
                attrs={
                    'id':'contraseñaColaborador',
                    'onkeyup':'contraseña()'
                }
            )
        }