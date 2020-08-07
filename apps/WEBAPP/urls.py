
from django.conf.urls import url
from apps.WEBAPP import views


urlpatterns = [
    url('/home', views.index, name="home"),
]