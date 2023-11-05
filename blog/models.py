from enum import unique
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid
# from django.urls import reverse

# creating new manager
class PublishedManager(models.Manager):
	def get_querryset(self):
		return super(PublishedManager,self).get_querryset().filter(status='published')

# Create your models here.
class Post(models.Model):
	STATUS_CHIOCES = ( 
		('draft','Draft'),
		('published','Published'),
		)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, on_delete=models.CASCADE, default='User', related_name='blog_posts')
	img = models.ImageField(upload_to='updates/')
	body = RichTextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHIOCES, default='published ')
	objects =models.Manager()
	published = PublishedManager()

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	@property
	def imgURL(self):
		try:
			url = self.img.url
		except:
			url =''
		return url
	
	def clean(self):
		super().clean()
		if self.img.width < 1920 or self.img.height < 1088:
			raise ValidationError("Image minimum dimensions should be at least 1920x1088 pixels.")
		elif self.img.width > 1920 or self.img.height > 1088:
			raise ValidationError("Image maximum dimensions should be at most 1920x1088 pixels.")

class Comment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80, blank=True, null=True)
	email= models.EmailField()
	body = models.TextField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)
	def __str__(self):
		return f'Comment by {self.name} on {self.post}'
	