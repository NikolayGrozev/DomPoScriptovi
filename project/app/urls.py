from django.urls import path
from . import views

urlpatterns = [
    path("counts", views.count, name="count")
]