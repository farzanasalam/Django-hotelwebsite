from django.shortcuts import render, redirect

from .forms import FoodForm
from .models import Food


# Create your views here.
def index(request):
    Food1 = Food.objects.all()
    context = {

        'food_list': Food1
    }
    return render(request, 'index.html', context)


def detail(request, food_id):
    food1 = Food.objects.get(id=food_id)
    return render(request, 'detail.html', {'food1': food1})


def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        rate = request.POST.get('rate')
        img = request.FILES['img']
        food2 = Food(name=name, desc=desc, rate=rate, img=img)
        food2.save()
    return render(request, 'add.html')


def update(request, id):
    food = Food.objects.get(id=id)
    form = FoodForm(request.POST or None, request.FILES, instance=food)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'food': food})


def delete(request, id):
    if request.method == 'POST':
        food = Food.objects.get(id=id)
        food.delete()
        return redirect('/')
    return render(request, 'delete.html')
