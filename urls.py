from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
path('post_list/', views.post_list, name="post_list"),
path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name="post_detail"),
]