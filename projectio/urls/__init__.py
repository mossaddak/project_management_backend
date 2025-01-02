from django.urls import path, include

urlpatterns = [path("", include("projectio.urls.projects"))]
