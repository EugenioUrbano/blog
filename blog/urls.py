from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]