from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    #Path del core
    path('services/', views.services,name ="services" ),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)