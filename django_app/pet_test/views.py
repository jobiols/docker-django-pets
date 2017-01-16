from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GuestForm, PetForm
from .models import ImportedData, Guests
import logging
logger = logging.getLogger('')

def index(request):
    form = GuestForm()
    return render(request, 'pet_test/index.html', {'form': form})

def get_pet_class(id):
    return 'perro'

def consult(request):
    if request.method == 'POST':
        guest_data = {}
        request.session['name'] = request.POST['name']
        # salvar los datos del invitado
        g = Guests(name=request.POST['name'],
                   mail=request.POST['mail'])
        g.save()

        guest_data['name'] = request.POST['name']
        guest_data['mail'] = request.POST['mail']
        guest_data['location'] = request.POST['location']
        guest_data['pet_class'] = get_pet_class(request.POST['pet'])
        guest_data['form'] = PetForm()
    else:
        return HttpResponseRedirect('/')

    return render(request, 'pet_test/consult.html', {'guest_data': guest_data})


def respuesta(request):
    if request.method == 'POST':
        answer = request.POST

    answer = {}
    answer['name'] = request.session.get('name')
    answer['pet_class'] = 'perro'
    answer['ImportedData'] = ImportedData.objects.all()
    return render(request, 'pet_test/respuesta.html', {'answer':answer})

