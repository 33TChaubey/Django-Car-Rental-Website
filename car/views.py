from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Car, Review, Features, Order, PrivateMsg
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CarForm, OrderForm, MessageForm, FeaturesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy


def home(request):
    cars = Car.objects.all()[:5]
    return render(request, 'pages/index.html', {"cars": cars})


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def cars(request):
    car = Car.objects.all()
    query = request.GET.get('q')
    if query:
        car = car.filter(
            Q(car_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(num_of_seats__icontains=query) |
            Q(cost_par_day__icontains=query)
        )
    paginator = Paginator(car, 9)
    page_number = request.GET.get('page', 1)
    try:
        cars = paginator.page(page_number)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        cars = paginator.page(1)

    return render(request, 'pages/cars.html', {"cars": cars})


def car_details(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'pages/cars-details.html', {"car": car})


@login_required
def car_created(request):
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("home")
    context = {
        "form": form,
        "title": "Create Car"
    }
    return render(request, 'car_create.html', context)


@login_required
def car_update(request, id=None):
    detail = get_object_or_404(Car, id=id)
    if request.user != detail.owner:
        return redirect('home')
    form = CarForm(request.POST, request.FILES, instance=detail)
    if form.is_valid():
        form.save()
        return redirect('cars-details', id)
    context = {
        "form": form,
        "title": "Update Car"
    }
    return render(request, 'car_create.html', context)


class CarUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'car-update.html'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)
    fields = ['car_name', 'company_name', 'num_of_seats', 'num_of_air_bag', 'fuel_type', 'mileage',
              'transmission', 'image', 'location', 'const_per_hour', 'cost_par_day', 'cost_of_leasing', 'description', 'is_avaliable']
    success_url = reverse_lazy('cars')


class CarCreate(LoginRequiredMixin, CreateView):
    template_name = 'car_create.html'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)
    fields = ['car_name', 'company_name', 'num_of_seats', 'num_of_air_bag', 'fuel_type', 'mileage',
              'transmission', 'image', 'location', 'const_per_hour', 'cost_par_day', 'cost_of_leasing', 'description', 'is_avaliable']
    success_url = reverse_lazy('cars')

    def form_valid(self, form: CarForm):
        car = form.save(commit=False)
        car.owner = self.request.user
        car.save()
        return HttpResponseRedirect(car.get_absolute_url())


@login_required
def car_delete(request, id=None):
    query = get_object_or_404(Car, id=id)
    if request.user != query.owner:
        return redirect('home')
    query.delete()

    car = Car.objects.all()
    context = {
        'car': car,
    }
    return render(request, 'admin_index.html', context)

# order


@login_required
def order_list(request):
    order = Order.objects.all()

    query = request.GET.get('q')
    if query:
        order = order.filter(
            Q(car__car_name__icontains=query) |
            Q(user__username__icontains=query)
        )

    # pagination
    paginator = Paginator(order, 4)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        order = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        order = paginator.page(paginator.num_pages)
    context = {
        'order': order,
    }
    return render(request, 'order_list.html', context)


@login_required
def order_detail(request, id=None):
    detail = get_object_or_404(Order, id=id)
    if request.user != detail.user and request.user == detail.car.owner:
        return redirect('home')
    context = {
        "detail": detail,
    }
    return render(request, 'order_detail.html', context)


@login_required
def order_created(request, id):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        car = Car.objects.get(id=id)
        instance.car = car
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": "Create Order"
    }
    return render(request, 'order_create.html', context)


@login_required
def order_update(request, id=None):
    detail = get_object_or_404(Order, id=id)
    if request.user != detail.user:
        return redirect('home')
    form = OrderForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Update Order"
    }
    return render(request, 'order_create.html', context)


@login_required
def order_delete(request, id=None):
    query = get_object_or_404(Order, id=id)
    if request.user != query.user:
        return redirect('home')
    query.delete()
    return redirect('order_list')


@login_required
def mycars(request):
    new = get_list_or_404(Car, owner=request.user)
    # seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(car_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(num_of_seats__icontains=query) |
            Q(cost_par_day__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'cars': new,
    }
    return render(request, 'new_car.html', context)


@login_required
def like_update(request, id=None):
    new = Car.objects.order_by('-id')
    like_count = get_object_or_404(Car, id=id)
    like_count.like += 1
    like_count.save()
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)


def popular_car(request):
    new = Car.objects.order_by('-like')
    # seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(car_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(num_of_seats__icontains=query) |
            Q(cost_par_day__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)


@login_required
def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We will contact you.')
            return redirect('contact')
    else:
        form = MessageForm()

    context = {
        'form': form,
        'title': 'Contact Us'
    }

    return render(request, 'contact.html', context)


# -----------------Admin Section-----------------

@login_required
def admin_car_list(request):
    car = Car.objects.order_by('-id')

    query = request.GET.get('q')
    if query:
        car = car.filter(
            Q(car_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(num_of_seats__icontains=query) |
            Q(cost_par_day__icontains=query)
        )

    # pagination
    paginator = Paginator(car, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        car = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        car = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        car = paginator.page(paginator.num_pages)
    context = {
        'car': car,
    }
    return render(request, 'admin_index.html', context)


@login_required
def admin_msg(request):
    msg = PrivateMsg.objects.order_by('-id')
    context = {
        "car": msg,
    }
    return render(request, 'admin_msg.html', context)


@login_required
def msg_delete(request, id=None):
    query = get_object_or_404(PrivateMsg, id=id)
    query.delete()
    return HttpResponseRedirect("/message/")
