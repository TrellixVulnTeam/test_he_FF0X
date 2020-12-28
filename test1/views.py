from django.shortcuts import render
from django.http import HttpResponse

app_name = 'test1'

def test1(request):
    return render(request, 'test1/test1.html')
