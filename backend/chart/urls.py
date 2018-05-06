from django.urls import path
from . import views

app_name = "chart"

urlpatterns = [
    path("", views.viewChart, name="index"),
    path("api/chart/", views.apiChart, name='chartApi'),
]
