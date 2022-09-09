from .import views
from django.urls import path


urlpatterns=[
path('register',views.register,name='register'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
path('ajax/load-cities/', views.load_cities, name='ajax_load_cities')
 ]