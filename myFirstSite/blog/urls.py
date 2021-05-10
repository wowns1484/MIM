from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='main'),
    path('next.html', views.next_list, name='next'),
    path('main.html', views.post_list, name='main'),
]
