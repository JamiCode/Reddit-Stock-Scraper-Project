from django.shortcuts import render

# Create your views here.
def index_view(request):
	ctx = {}
	return render(request, "wallstreetbets.html", ctx)