from django.shortcuts import render
from .models import Car, Sale
from .forms import SaleForm
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.shortcuts import render



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car_list')  # Замінити на потрібний маршрут
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('car_list')  # Замінити на потрібний маршрут
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class CarListView(ListView):
    model = Car
    template_name = 'mashinki.html'
    context_object_name = 'cars'



class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'


class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale.html'
    context_object_name = 'form'

    def car_list(request, category=None):
        if category:
            cars = Car.objects.filter(category=category)
        else:
            cars = Car.objects.all()
        return render(request, 'cars/mashinki.html', {'cars': cars})

    # Визначаємо метод для обробки додаткових даних у формі
    def form_valid(self, form):
        # Отримуємо автомобіль через car_id з URL
        car = get_object_or_404(Car, id=self.kwargs['car_id'])

        # Зв'язуємо створений продаж з автомобілем та задаємо ціну
        sale = form.save(commit=False)
        sale.car = car
        sale.total_price = car.price
        sale.save()

        # Повертаємо підтвердження створення продажу
        return render(self.request, 'sale_confirm.html', {'sale': sale})

    # Для передачі додаткової інформації (наприклад, автомобіля) в шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = get_object_or_404(Car, id=self.kwargs['car_id'])
        context['car'] = car
        return context

def about(request):
    return render(request, 'About_us.html')
