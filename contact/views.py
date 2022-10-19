from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import *


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


# def contact(request):
#     return render(request, 'contact/contact.html')