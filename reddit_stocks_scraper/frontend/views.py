from django.shortcuts import render

# Create your views here.
def home_view(request):
	ctx = {}
	return render(request, "frontend/home.html", ctx)

