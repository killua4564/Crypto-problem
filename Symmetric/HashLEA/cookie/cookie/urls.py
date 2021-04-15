from django.urls import path

from . import views

urlpatterns = [
	path('admin/', views.admin),
    path('index/', views.index),
]
