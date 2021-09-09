from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('services',views.services,name='services'),
    path('aboutus',views.about,name='aboutus'),
    path('gallery',views.gallery,name='gallery'),
    path('index',views.index,name="home"),
    path('contactus',views.contactus,name='contactus'),
    path('gymnastic',views.gymnastic,name='gymnastic'),
    path('calisthenic',views.calisthenic,name='calisthenic')
]