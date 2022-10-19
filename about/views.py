from django.shortcuts import render
from .models import *


def about(request):
    about_list = AboutModel.objects.all()

    context = {
        'about_list': about_list,
    }
    return render(request, 'about/about.html', context)
