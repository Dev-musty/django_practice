from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

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


@require_POST
def delete_car(request, car_id):
	car = get_object_or_404(Car, id=car_id)
	car.delete()
	return redirect('car-list')
