from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def offer(request):
	return render(request, 'offer.html')

def products(request):
	return render(request, 'products.html')

def projects(request):
	return render(request, 'projects.html')

def contact(request):
	return render(request, 'contact.html')

def gallery(request):
	return render(request, 'gallery.html')