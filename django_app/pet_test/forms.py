# -*- coding: utf-8 -*-

from django import forms

PET_CHOICES = (
    (1, 'Perro'),
    (2, 'Gato'),
    (3, 'Tortuga'),
    (4, 'Pajarito'),
)

PET_RAZAS = (
    (1,'Otros'),
    (2,'Boxer'),
)
PET_SIZES = (
    (1,'Pequeño'),
    (2,'Mediano'),
)
PET_AGE = (
    (1,'bebe'),
    (2,'anciano'),
)

class GuestForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, required=True)
    location = forms.CharField(label='Localidad', max_length=100, required=True)
    mail = forms.EmailField(required=True)
    pet = forms.ChoiceField(choices=PET_CHOICES, label='Mascota')

class PetForm(forms.Form):
    raza = forms.ChoiceField(choices=PET_RAZAS, label='Raza')
    size = forms.ChoiceField(choices=PET_SIZES,label='Tamaño')
    age  = forms.ChoiceField(choices=PET_AGE,label='Edad')