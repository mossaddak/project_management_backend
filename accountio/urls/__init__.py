from django.urls import path, include

urlpatterns = [path("", include("accountio.urls.users"))]
