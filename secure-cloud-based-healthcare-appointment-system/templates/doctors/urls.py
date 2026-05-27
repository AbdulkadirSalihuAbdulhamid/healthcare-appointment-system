# doctors/urls.py
from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
    path("", views.doctor_list, name="doctor-list"),                 # /doctors/
    path("search/", views.doctor_search, name="doctor-search"),      # /doctors/search/?q=&city=&specialty=
    path("<str:username>/", views.doctor_profile, name="doctor-profile"),  # /doctors/<username>/
]
