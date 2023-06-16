from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("letters/create/", views.create_letter, name="create_letter"),
    path("letters/", views.list_letter, name="list_letter"),
    path("letters/<int:letter_id>", views.detail_letter, name="detail_letter"),
    path("letters/success/", views.success_letter, name="success_letter"),
]