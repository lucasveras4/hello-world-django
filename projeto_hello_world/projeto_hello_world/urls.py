from django.urls import path
from app_hello_world import views

urlpatterns = [
    path('',views.home,name='home' ),
]
