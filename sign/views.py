from django.shortcuts import render
from django.http import HttpResponse
from sper import kk

# Create your views here.
def ji(request):
    cc=kk()
    return render(request,"ji.html",{"pp":cc})
def index(request):

    return  render(request,"index.html")