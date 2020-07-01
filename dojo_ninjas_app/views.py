from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
  context = {
    "dojos": Dojo.objects.all(),
    "ninjas": Ninja.objects.all(),
  }
  return render(request, 'index.html', context)

def process(request):
  Dojo.objects.create(
    name= request.POST['name'],
    city= request.POST['city'],
    state= request.POST['state']
  )
  return redirect('/')

def create(request):
  request.session['dojo_id'] = request.POST['dojo']
  dojo_in_session = Dojo.objects.get(id= request.session['dojo_id'])
  Ninja.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], dojo= dojo_in_session)
  return redirect('/')

def delete_dojo(request):
  removed_dojo = Dojo.objects.get(id= request.POST['remove'])
  removed_dojo.delete()
  return redirect('/')