from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .models import *


@cache_page(60 * 15)
def services(request):
    services_list = ServicesModel.objects.all()

    contex = {
        'services_list': services_list,
    }
    return render(request, 'services/services.html', contex)
