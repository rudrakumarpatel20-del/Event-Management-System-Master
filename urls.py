"""SCM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# 1. Primary URL Dispatcher
urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Main Application (scmapp)
    path('', include('scmapp.urls')),
]

# 2. Media & Static Asset Configuration
# This block allows Django to serve files like event photos and CSS 
# directly from your local Windows directory during development.
if settings.DEBUG:
    # Serving user-uploaded files (Event Photos)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Serving static assets (CSS, JS, Logos)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    