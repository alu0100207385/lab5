# Create your views here.

#from django.http import HttpResponse
#def test_home(request):
	#return HttpResponse("Estas en Home");

#def test_help(request):
	#return HttpResponse("Estas en Help");

#def test_about(request):
	#return HttpResponse("Estas en About");
      
from django.shortcuts import render_to_response

def test_home(request):
	return render_to_response("home.html", {})
      
def test_help(request):
	return render_to_response("help.html", {})
      
def test_about(request):
	return render_to_response("about.html", {})
     
