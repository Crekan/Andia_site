from django.shortcuts import render
from .models import *


def index(request):
    sliders = SliderModel.objects.all()
    cards = CardsBenefitsModel.objects.all()
    latest_works = LatestWork.objects.all()

    context = {
        'sliders': sliders,
        'cards': cards,
        'latest_works': latest_works,
    }
    return render(request, 'slider/index.html', context)
