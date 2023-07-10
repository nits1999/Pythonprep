from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {

        'author': 'John',
        'title': 'Blog 1',
        'content': ' this is a new content',
        'date_posted': 'June 21, 2023'
    },
    {

        'author': 'Wick',
        'title': 'Blog 2',
        'content': ' this is a new content for blog2',
        'date_posted': 'June 29, 2023'
    },
]







# Create your views here.
def home(request):
	context = {
	    'posts':posts
	}
	return render(request,'blog/home.html', context)

def about(request):
	return render(request,'blog/about.html',{'title': 'about'})
