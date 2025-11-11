# Create your views here.
from django.shortcuts import render
'''from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
'''
# Modify the View
'''from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
'''
def members(request):
    return render(request, 'members/myfirst.html')
