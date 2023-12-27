import json

from django.shortcuts import render
from .forms import RanGenForm

import requests


def sendREQ(request, count_num):
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
    form = RanGenForm(request.POST or None, request.FILES or None)
    ticket = sendREQ(request, count_num=5)
    print(ticket)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'rangen/index.html', context)
