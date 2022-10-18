from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


# class Portfolio(ListView):
#     model = PortfolioModel
#     template_name = 'portfolio/portfolio.html'
#     context_object_name = 'portfolio_list'
#
#     def get_queryset(self):
#         return PortfolioModel.objects.all()
#
#
# class PortfolioCategorise(ListView):
#     model = PortfolioModel
#     template_name = 'portfolio/portfolio.html'
#     context_object_name = 'portfolio_list'
#     allow_empty = False
#
#     def get_queryset(self):
#         return PortfolioModel.objects.filter(cat_id=self.kwargs['cat_id'])

def portfolio(request):
    cats = Categories.objects.all()
    portfolio_list = PortfolioModel.objects.all()

    context = {
        'cats': cats,
        'portfolio_list': portfolio_list,
        'cat_selected': 0,
    }

    return render(request, 'portfolio/portfolio.html', context)


def show_categories(request, cat_id):
    portfolio_list = PortfolioModel.objects.filter(cat_id=cat_id)
    cats = Categories.objects.all()

    context = {
        'portfolio_list': portfolio_list,
        'cats': cats,
        'cat_selected': cat_id,
    }

    return render(request, 'portfolio/portfolio.html', context)
