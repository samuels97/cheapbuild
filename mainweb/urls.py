from django.urls import path
from .import views

app_name = 'mainweb'
urlpatterns = [
path("",views.Home_view, name="homepage"),
path('about/',views.About_View, name="Aboutpage"),

path('service/', views.Service_view, name="servicepage"),
path('service_details/<str:pk_serv>/', views.Service_details_view, name="service_details"),

path('team/', views.Team_view, name="teampage"),

path('projects/', views.Project_view, name="projectspage"),

path('project_details/<str:pk_proj>/', views.Project_Detail_view, name="project_details"),

path('blog/', views.Blog_view, name="blogpage"),
path('blog_details/', views.Blog_detview, name="blog_detailspage"),
path("contact/",views.Contact_view, name="contactpage"),

]