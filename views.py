from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def error_404_view(request,exception):
	return redirect('Does not exist')

def post_list(request):
	object_list = Post.published.all()
	paginator = Paginator(object_list,3)
	page = request.GET.get('page')

	try:

		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'blog/list.html', {'page':page,'posts':posts})

def post_detail(request,year,month,day,post):
	post = get_object_or_404(Post, slug=post,status='Published')
	return render(request, 'blog/detail.html',{'post':post}) 