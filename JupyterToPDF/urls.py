"""JupyterToPDF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls import url
from django.conf.urls.static import static
from apps.APIREST import urls as urls_api_rest
# from apps.WEBAPP import urls as urls_web_app
from apps.WEBAPP import views as views_web_app

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views_web_app.index, name="home"),
    url(settings.BASE_API, include(urls_api_rest)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)