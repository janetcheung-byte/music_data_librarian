from django.urls import path
from . import views

urlpatterns = [
    path("", views.ingest_data_view, name="home"),  # Root path for /music_library/
    path("ingest_data/", views.ingest_data_view, name="ingest_data"),  # Path for /music_library/ingest_data/
    path("generate_report/", views.generate_report_view, name="generate_report"),  # Path for /music_library/generate_report/
]
