from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^classdetail/$', views.classdetail, name='classdetail'),
    url(r'^checkout/$', views.checkoutPage, name='checkoutPage'),
]
