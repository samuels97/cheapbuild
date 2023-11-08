from django.urls import path
from .import views

app_name = "blog"

urlpatterns = [
    path('', views.Updates_list, name="blog_list"),
    path('tag/<slug:tag_slug>',views.Updates_list, name="post_list_tag"),
    path('updates/<str:pk>/', views.Update_details_view, name='detailspage'),

]