from django.urls import path     
from . import views
urlpatterns = [
    path('', views.red_to_time_display),
    path('time_display', views.index)
]