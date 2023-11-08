from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from.models import Post,Comment
from.forms import CommentForm
from taggit.models import Tag
from mainweb.models import *

# Create your views here.

def error_404_view(request,exception):
	return HttpResponse('Does Not Exist')

def Updates_list(request, tag_slug=None):
	locate = Location.objects.all()
	emailz = Email.objects.all()
	phones = OfficePhone.objects.all()
	posts = Post.objects.all()

	# pagination
	paginator =Paginator(posts,10)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	tag = None

	if tag_slug:
		tag = get_object_or_404(Tag,slug=tag_slug)
		post = post.filter(tags__in=[tag])

	context = {
		'posts':posts,'page':page,'tag':tag,
		'locate':locate,'emailz':emailz,'phones':phones
	}
	return render(request, 'blog/index.html', context)



def Update_details_view(request,pk):

	locate = Location.objects.all()
	emailz = Email.objects.all()
	phones = OfficePhone.objects.all()
	post = Post.objects.get(id=pk)

	posts = Post.objects.all()
	# display all post commets
	comments= post.comments.filter(active=True)
	new_comment = None

	# adding comments

	if request.method =='POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
			return redirect('blog:blog_list') 
	else:
		comment_form = CommentForm()
	
	context = {
		'post':post,'posts':posts, 'comments':comments
		,'comment_form':comment_form,'new_comment':new_comment,
		'locate':locate,'emailz':emailz,'phones':phones
		}
	return render(request, 'blog/update_details.html', context)
