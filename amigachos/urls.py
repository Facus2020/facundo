from django.urls import path
from . import views

urlpatterns = [
    path('', views.persona_list, name='persona_list'),
]