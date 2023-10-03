from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    #Path del core
    path('', views.home,name ="home" ),
    path('about/', views.about,name ="about" ),
    path('store/', views.store,name ="store" ),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)