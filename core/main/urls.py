from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:article_id>/download/', views.download_article, name='download_article'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]