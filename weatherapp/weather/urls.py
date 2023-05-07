from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #path for our index view
    path('about/', views.about)
]