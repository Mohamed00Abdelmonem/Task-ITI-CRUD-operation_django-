from django.db.models import Q
from django.shortcuts import render, redirect
from .models import car
from .forms import CAR


# Create your views here.
def home(request):
    cars = car.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        cars = car.objects.filter(Q(color__icontains=q))

    return render(request, 'home.html', {'cars': cars})


# def create(request):
#     return render(request, 'create.html')


def create(request):
    if request.method == 'POST':
        form = CAR(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = CAR()

    return render(request, 'create.html', {'form': form})


def update(request, id):
    Car = car.objects.get(id=id)
    form = CAR(instance=Car)
    context = {'form': form}

    if request.method == 'POST':
        form = CAR(request.POST, request.FILES, instance=Car)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'create.html', context)


def delete(request, id):
    Car = car.objects.get(id=id)
    Car.delete()
    Car = car.objects.all()

    return render(request, 'home.html', {'cars': Car})
