from django.urls import path
from .import views

app_name = "blog"

urlpatterns = [
    path('', views.Updates_list, name="blog_list"),
]