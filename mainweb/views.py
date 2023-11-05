from django.shortcuts import render
from.models import*
from .utils import get_contact_info
# Create your views here.

def Home_view(request):
	context = get_contact_info()
	return render(request, 'mainweb/index.html',context)

def About_View(request):
	context = get_contact_info()
	return render(request, 'mainweb/about.html',context)

def Project_view(request):
	context = get_contact_info()
	return render(request, 'mainweb/projects.html',context)

def Project_Detail_view(request,pk_proj):
	projectz = Projects.objects.get(id=pk_proj)

	return render(request, 'mainweb/project_details.html',{'projectz':projectz})


def Service_view(request):

	context = get_contact_info()	
	return render(request ,'mainweb/services.html',context)

def Service_details_view(request,pk_serv):
	service = Services.objects.get(id=pk_serv)

	context = {'service':service}
	return render(request, 'mainweb/service_details.html',context)
	

def Team_view(request):
	team    = Staff.objects.filter().order_by('department')
	context = {'team':team}
	return render(request, 'mainweb/team.html',context)


def Contact_view(request):
	context = get_contact_info()
	return render(request, 'mainweb/contact.html',context)

