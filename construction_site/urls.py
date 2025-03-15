"""
URL configuration for construction_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.urls import include, path
from contact import views  # Import views from your 'contact' app
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),  # Keep this for the contact page
    path('', views.home, name='home'),  # Add this for the homepage
    path('about/', views.about, name='about'),  
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('sitemap.xml', RedirectView.as_view(url='/static/sitemap.xml', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

