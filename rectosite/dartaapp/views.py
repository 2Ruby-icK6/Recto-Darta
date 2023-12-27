from django.shortcuts import render
from django.views.generic.list import ListView
from dartaapp.models import BookDetail

# Create your views here.
class HomePageView(ListView):
    model = BookDetail
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context