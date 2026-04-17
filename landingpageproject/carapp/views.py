from django.shortcuts import redirect, render

from .forms import CarForm
from .models import Car

def landing_page(request):
	return render(request, 'carapp/landing.html')


def add_car(request):
	if request.method == 'POST':
		form = CarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('car-list')
	else:
		form = CarForm()

	return render(request, 'carapp/add_car.html', {'form': form})


def car_list(request):
	cars = Car.objects.all().order_by('-id')
	return render(request, 'carapp/car_list.html', {'cars': cars})
