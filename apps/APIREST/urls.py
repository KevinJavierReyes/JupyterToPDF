from django.urls import path
from .views import JupyterToPDF

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("/convert/JupyterToPDF", JupyterToPDF.as_view()),
]
