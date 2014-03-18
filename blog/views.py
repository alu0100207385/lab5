# Create your views here.

from django.http import HttpResponse
#def test_home(request):
	#return HttpResponse("Estas en Home");
      
      
from django.shortcuts import render_to_response

def test_home(request):
	return render_to_response("blog.html", {})
     

def test_help(request):
	return HttpResponse("Estas en Help");

def test_about(request):
	return HttpResponse("Estas en About");