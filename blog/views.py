from django.shortcuts import render
from .models import Post, Food


# Create your views here.
def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')

def search(request):
	print(request.GET)
	print(request.POST)
	my_new_title = request.POST.get('title')
	print(my_new_title)
	if my_new_title:
		match =Food.objects.filter(name__contains=my_new_title)
		print("match", match)
	context = {}
	return render(request, 'blog/search.html')

