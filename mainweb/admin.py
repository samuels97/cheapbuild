from django.contrib import admin
from .models import*

# services offered
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
	list_display = ('title','publish')
	list_filter = ('created','publish','updated')
	search_Fields = ('title','body')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'
	ordering = ('publish',)
# service caption
@admin.register(ServeCaptin)
class ServeCaptinAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_filter = ('created','updated')
	search_Fields = ('title',)
	date_hierarchy = 'created'
	ordering = ('created',)
# who we are
@admin.register(Who)
class WhoAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug','publish','since')
	list_filter = ('created','publish','updated')
	search_Fields = ('title','body')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'
	ordering = ('publish',)

# projects
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
	list_display = ('title', 'status','publish','started','design_view')
	list_filter = ('created','publish','status')
	search_Fields = ('title','body')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'
	ordering = ('publish',)
# why choos us
@admin.register(ChoozeUs)
class ChoozeUsAdmin(admin.ModelAdmin):
	list_display = ('tag','created','updated')
	list_filter = ('created','updated')

# staff or team
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug','email','join_date','department')
	list_filter = ('created','publish','department')
	search_Fields = ('role','description','created')
	prepopulated_fields = {'slug': ('name',)}
	date_hierarchy = 'publish'
	ordering = ('publish',)

# phones
@admin.register(OfficePhone)
class OfficePhoneAdmin(admin.ModelAdmin):
	list_display = ('Phone_number','describe_Phone_number','created','updated')
	list_filter = ('created',)
	search_Fields = ('Phone_number',)
	date_hierarchy = 'created'
	ordering = ('created',)


# emails 
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
	list_display = ('email','describe_email','created','updated')
	list_filter = ('created',)
	search_Fields = ('email',)
	date_hierarchy = 'created'
	ordering = ('created',)


# emails 
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ('Company_name','P_o_box_no','created','updated')
	list_filter = ('created',)
	search_Fields = ('Company_name',)
	date_hierarchy = 'created'
	ordering = ('created',)

@admin.register(background)
class backgroundAdmin(admin.ModelAdmin):
	list_display = ('created_by','is_published','created','updated')
	list_filter = ('created',)
	search_Fields = ('created_by',)
	date_hierarchy = 'created'
	ordering = ('created',)


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
	list_display = ('name','role','created','updated')
	list_filter = ('created',)
	search_Fields = ('name',)
	date_hierarchy = 'created'
	ordering = ('created',)

# 
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
	list_display = ('title','deadline','publish','created','updated')
	list_filter = ('created',)
	search_Fields = ('title',)
	date_hierarchy = 'created'
	ordering = ('publish',)

# 

@admin.register(backgroudImages)
class backgroudImagesAdmin(admin.ModelAdmin):
	list_display = ('title','created','updated')
	list_filter = ('created',)
	search_Fields = ('title',)
	date_hierarchy = 'created'
	ordering = ('-created',)

@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
	list_display = ('categories','created','updated')
	list_filter = ('created',)
	search_Fields = ('categories',)
	date_hierarchy = 'created'
	ordering = ('-created',)

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
	list_display = ('body','created','updated')
	list_filter = ('created',)
	date_hierarchy = 'created'
	ordering = ('-created',)


@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
	list_display = ('body','created','updated')
	list_filter = ('created',)
	date_hierarchy = 'created'
	ordering = ('-created',)

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
	list_display = ('body','created','updated')
	list_filter = ('created',)
	date_hierarchy = 'created'
	ordering = ('-created',)


@admin.register(messages)
class messagesAdmin(admin.ModelAdmin):
	list_display = ('name','email','subject','created')
	list_filter = ('created',)
	search_Fields = ('subject',)
	date_hierarchy = 'created'
	ordering = ('created',)