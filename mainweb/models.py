from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
import uuid

# Create your models here.


class Timez(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True  # Make Timez model abstract

class background(Timez):
	title = models.CharField(max_length=254, blank=True, null=True)
	descriptions = RichTextField()
	created_by = models.CharField(max_length=200)
	is_published = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = '01. Background'

	def __str__(self):
		return self.title

class backgroudImages(Timez):
	title = models.ForeignKey(background, on_delete=models.CASCADE, blank=True)
	image = models.ImageField(upload_to='back', null=True, blank=True)

	class Meta:
		verbose_name_plural = '02. Back Images'

	def clean(self):
		super().clean()
		if self.image.width != 400 or self.image.height != 600:
			raise ValidationError("Image dimensions should be at least 400x600 pixels.")
		elif self.image.width != 400 or self.image.height != 600:
			raise ValidationError("Image dimensions should be at most 400x600 pixels.")


class ChoozeUs(Timez):
	tag                 = models.CharField(max_length=200)
	description         = RichTextField()
	
	class Meta:
		verbose_name_plural = '03. Why Choose us'

	def __str__(self):
		return self.tag


class Email(Timez):
    email= models.EmailField(unique=True)
    describe_email = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = '04. Emails'

    def __str__(self):
        return self.email

class OfficePhone(Timez):
    Phone_number= models.CharField(max_length=13, unique=True)
    describe_Phone_number = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = '05. Office Phones'

    def __str__(self):
        return self.Phone_number


class Location(Timez):   
    Company_name = models.CharField(max_length=200,unique=True)
    P_o_box_no = models.CharField(max_length=200,unique=True)

    class Meta:
        verbose_name_plural = '06. Location'

    def __str__(self):
        return self.Company_name


class Banners(Timez):
    CATE = (
		('home','home'),
	)
    categories = models.CharField(max_length=200, choices=CATE)
    image = models.ImageField(upload_to='banners/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    class Meta:
        verbose_name_plural = '07. Banners'
    
    def __str__(self):
        return self.categories
    

    def clean(self):
        super().clean()
        if self.image.width != 1920 or self.image.height != 1080:
            raise ValidationError("Image dimensions should be at least 1920x1088 pixels.")
        elif self.image.width != 1920 or self.image.height != 1080:
            raise ValidationError("Image dimensions should be at most 1920x1088 pixels.")




# Create your models here.
class PublishedManager(models.Manager):
	def get_querryset(self):
		return super(PublishedManager,self).get_querryset().filter(status='published')
		return self.title



class ServeCaptin(Timez):
	title        = models.CharField(max_length=200,null=True, blank=True)

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name_plural = '08. Services Caption'

class Services(Timez):
	title        = models.CharField(max_length=200,null=True, blank=True)
	slug         = models.SlugField(max_length=200, unique_for_date='publish')
	body         = RichTextField()
	image        = models.ImageField(upload_to='media/Services', null=True, blank=True) 
	publish      = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = '09. Services'

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	def clean(self):
		super().clean()
		if self.image.width < 550 or self.image.height < 550:
			raise ValidationError("Image minimum dimensions should be at least 550X550 pixels.")
		elif self.image.width > 550 or self.image.height > 550:
			raise ValidationError("Image  dimensions should be at most 550X550 pixels.")


class Projects(Timez):
	STATUS_CHOICES = (
		('finshed', 'Finished'),
		('pending', 'Pending'),
		)
	VIEW_CHOICES = (
		('interior', 'Interior'),
		('exterior', 'Exterior'),
		)

	title        = models.CharField(max_length=200)
	slug         = models.SlugField(max_length=200, unique_for_date='publish')
	design_view  = models.CharField(choices=VIEW_CHOICES, max_length=225)
	body         = RichTextField()
	image        = models.ImageField(upload_to='media/projcects') 
	publish      = models.DateTimeField(default=timezone.now)
	status       = models.CharField(max_length=10, choices=STATUS_CHOICES, default='finshed')
	started      = models.DateField(default=timezone.now)
	
	class Meta:
		verbose_name_plural = '10. Projects'

	def __str__(self):
		return self.title

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	def clean(self):
		super().clean()
		if self.image.width < 400 or self.image.height < 500:
			raise ValidationError("Image minimum dimensions should be at least 400x500 pixels.")
		elif self.image.width > 400 or self.image.height > 500:
			raise ValidationError("Image  dimensions should be at most 400x500 pixels.")

	
class Who(Timez):
	title        = models.CharField(max_length=200)
	slug         = models.SlugField(max_length=200, unique_for_date='publish')
	body         = RichTextField()
	image        = models.ImageField(upload_to='media/who') 
	publish      = models.DateTimeField(default=timezone.now)
	since        = models.DateField(auto_now_add=False)

	class Meta:
		verbose_name_plural = '11. Who we are'

	def __str__(self):
		return self.title

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	def clean(self):
		super().clean()
		if self.image.width < 1920 or self.image.height < 1088:
			raise ValidationError("Image minimum dimensions should be at least 1920x1088 pixels.")
		elif self.image.width > 1920 or self.image.height > 1088:
			raise ValidationError("Image  dimensions should be at most 1920x1088 pixels.")


class Staff(Timez):
	DEPARTMENTS = (
		('magement', 'Magement'),
		('survey', 'survey'),
		('steel', 'Steel'),
		('contruction', 'Contruction'),
		('finishing', 'Finishing'),
		)
	name = models.CharField(max_length=256)
	slug = models.SlugField(max_length=200, unique_for_date='publish')
	email = models.EmailField(blank=True)
	post = models.CharField(max_length=256 )
	role = models.CharField(max_length=256 )
	description = RichTextField()
	twitter = models.URLField(max_length=200,blank=True, null=True)
	faceBook = models.URLField(max_length=200,blank=True, null=True)
	instagram = models.URLField(max_length=200,blank=True, null=True)
	linkedin = models.URLField(max_length=200,blank=True, null=True)
	publish = models.DateField(default=timezone.now)
	image = models.ImageField(upload_to='media/staff') 
	department = models.CharField(max_length=256,choices=DEPARTMENTS, default='contruction')
	join_date = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = '12. Team Members'

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	def clean(self):
		super().clean()
		if self.image.width < 550 or self.image.height < 600:
			raise ValidationError("Image minimum dimensions should be at least 550x600 pixels.")
		elif self.image.width > 550 or self.image.height > 600:
			raise ValidationError("Image  dimensions should be at most 550x600 pixels.")



class Testimony(Timez):
	name = models.CharField(max_length=256)
	testify = RichTextField()
	role = models.CharField(max_length=256)

	class Meta:
		verbose_name_plural = '13. Testimonies'

	def __str__(self):
		return self.name


class Career(Timez):
	title        = models.CharField(max_length=200,null=True, blank=True)
	description  = RichTextField()
	deadline     = models.DateTimeField(default=timezone.now)
	publish      = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = '14. Careers'
	def __str__(self):
		return self.title


class Mission(Timez):
	body        = models.CharField(max_length=254,null=True, blank=True)

	class Meta:
		verbose_name_plural = '15. Mission'

	def __str__(self):
		return self.body

class Vision(Timez):
	body        = models.CharField(max_length=254,null=True, blank=True)

	class Meta:
		verbose_name_plural = '16. Vision'
	def __str__(self):
		return self.body

class Objective(Timez):
	body = RichTextField()

	class Meta:
		verbose_name_plural = '17. main objective'
	def __str__(self):
		return self.body


class messages(Timez):
	name = models.CharField(max_length=256)
	email = models.EmailField(max_length=254)
	subject = models.CharField(max_length=256)
	message = models.TextField()

	class Meta:
		verbose_name_plural = '18. Read Messages'

	def __str__(self):
		return self.name