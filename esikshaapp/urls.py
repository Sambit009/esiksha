from django.urls import path
from esikshaapp import views
from django.conf.urls import include
urlpatterns = [
    path('',views.comingsoon),
    ]
