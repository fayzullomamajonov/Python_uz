"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("admin/", admin.site.urls),
    path("registration/", include("registration_app.urls")),
>>>>>>> 1eb7c19f1849efd13f6412256b8a7beb11defd4f
=======
>>>>>>> 40ad829559cd3f96fdf325cbead63b28312f4322
    path("", include("course_app.urls")),
    path("registration/", include("registration_app.urls")),

=======
    path("", include("course_app.urls")),
    path("registration/", include("registration_app.urls")),
>>>>>>> 927edc9c27f90b9e321fe712c9bf92d1c9929a77
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
