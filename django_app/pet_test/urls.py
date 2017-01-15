from django.conf.urls import url

from . import views

#app_name = 'pet_test'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'consult/$', views.consult, name='consult'),
    url(r'respuesta/$', views.respuesta, name='respuesta'),
]