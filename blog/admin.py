from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','author','publish','created','updated','status')
	list_filter = ('status', 'created', 'author')
	search_fields = ('title','created')
	prepopulated_fields = {'slug': ('title',)}
	# raw_id_fields = ('author',)

	date_hierarchy = 'publish'
	ordering = ('publish', 'status',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active','email','body')

