from django.urls import path
from . import views

app_name = "chart"

urlpatterns = [
    path("", views.viewMainPage, name="index"),
    path("api/chart/", views.viewChartAPI.as_view(), name='chartApi'),
]
