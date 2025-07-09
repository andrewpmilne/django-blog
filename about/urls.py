from django.urls import path
from .views import get_about

urlpatterns = [
    path('', get_about, name='about'),
]
