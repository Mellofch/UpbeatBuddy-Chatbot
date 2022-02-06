from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.loginPage, name='login'),
    # TODO create a chatpage
    path('chatpage/', views.chatpage, name='chatpage'),
]
