from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('s_home/' ,views.simulation_home, name='s_home'),
    path('s_select/' ,views.simulation_select, name='s_select'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)