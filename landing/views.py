from doctest import REPORT_NDIFF
from django.shortcuts import render

def landing(request):
    return render(request, "landing/index.html")
