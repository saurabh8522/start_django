from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.http import HttpResponse
from . import models
# Create your views here.
# def index(request):
#     return render(request,'index.html')
class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context





class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')
