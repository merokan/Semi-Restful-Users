from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),  #display all users, GET
    url(r'^users$', views.index), #display form, GET
    url(r'^users/new$', views.new),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^users/create$', views.create), #POST
    url(r'^users/(?P<user_id>\d+)/destroy$', views.destroy),
    url(r'^users/(?P<user_id>\d+)/update$', views.update) #POST
]