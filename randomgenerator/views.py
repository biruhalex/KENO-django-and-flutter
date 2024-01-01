# import json
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect

from ran_gen_algorithm import Keno
from .forms import RanGenForm
from .models import RanGenModel
import random

from django.views import generic
import requests
import simplejson as json


def sendREQ(request):
    models = json.JSONDecoder()
    a = 'http://www.randomnumberapi.com/api/v1.0/random?min=1&max=80&count=5'
    API_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/audi?format=json"
    try:
        r = requests.get(a)
        models = r.json()
    except:
        print(f"Fetch models from {a} failed")
    return models


def ran_gen_view(request):
    context = {}
    keno = Keno(request)
    # keno.iterate()
    keno.lst_iteration()
    form = RanGenForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        for i in range(1000):
            ticket = sendREQ(request)
            my_string = ','.join(str(i) for i in ticket)
            RanGenModel.objects.create(my_list=my_string)
            print("ticket= " + str(ticket))
        form = RanGenForm()
    context['form'] = form
    return render(request, 'rangen/index.html', context)


def book_detail_view(request, num):
    try:
        model = RanGenModel.objects.get(pk=num)
    except RanGenModel.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'rangen/detail.html', context={'ran_num': model})


def ticket_list_view(request):
    queryset = RanGenModel.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "rangen/list.html", context)


def ticket_update_view(request):
    for i in range(200):
        print(i)
        i = i + 1
        obj = get_object_or_404(RanGenModel, id=i)
        print(obj.name)
        if obj.id < 201:
            obj.name = 'Gudisa'
            print(obj.name)
            obj.game_id = "5206"
            obj.save()
    for i in range(400):
        i = i + 1
        obj = get_object_or_404(RanGenModel, id=i)
        print(obj.name)
        if 401 > obj.id > 201:
            obj.name = 'Megersa'
            obj.game_id = "3208"
            obj.save()
    for i in range(600):
        i = i + 1
        obj = get_object_or_404(RanGenModel, id=i)
        print(obj.name)
        if 601 > obj.id > 401:
            obj.name = 'Tadele'
            obj.game_id = "1201"
            obj.save()
    for i in range(800):
        i = i + 1
        obj = get_object_or_404(RanGenModel, id=i)
        print(obj.name)
        if 801 > obj.id > 601:
            obj.name = 'Marta'
            obj.game_id = "9204"
            obj.save()
    for i in range(1000):
        i = i + 1
        obj = get_object_or_404(RanGenModel, id=i)
        print(obj.name)
        if 1001 > obj.id > 801:
            obj.name = 'Lilise'
            obj.game_id = "7205"
            obj.save()
    queryset = RanGenModel.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "rangen/list.html", context)


def update_ticket_price(request):
    obj = RanGenModel.objects.all()
    obj_count = obj.count()
    print('obj count - ', obj_count)
    lst = [10, 20, 30, 40, 50, 60, 70, 80,
           90, 100, 1000, 2000, 3000, 4000, 5000, 10000]
    for value in range(obj_count):
        value = value + 1
        print(value)
        o = obj.get(id=value)
        o.stake = random.sample(lst, 1)[0]
        o.win = 300 * o.stake
        print(o.win)
        print(o.stake)
        o.save()
    return redirect(ticket_list_view)

