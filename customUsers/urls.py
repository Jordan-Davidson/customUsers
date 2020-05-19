from django.urls import path
from customUsers import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.loginview),
    path('signup/', views.signup)
]