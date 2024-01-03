
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home',views.home , name="home"),
    path("admin/", admin.site.urls), 
    path('login',views.login , name="login"),
    path("register",views.register, name="register")    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()