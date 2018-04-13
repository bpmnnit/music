from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('<h1>This is the homepage of the music app.</h1>')