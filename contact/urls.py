from django.urls import path
from .views import contact_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView



urlpatterns = [
    path('contact/', contact_view, name='contact'),
   
]

