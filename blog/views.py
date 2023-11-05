from django.shortcuts import render

# Create your views here.

def Updates_list(request, tag_slug=None):
	
	context = {}
	return render(request, 'blog/index.html', context)
