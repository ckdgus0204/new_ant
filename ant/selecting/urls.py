from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('selecting_home/' ,views.selecting_home, name='selecting_home'),
    path('reflash/' ,views.reflash, name='reflash'),
    path('add_autoset',views.add_Autoset, name='add_autoset'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)