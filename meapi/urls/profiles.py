from django.urls import path

from ..views.profiles import PrivateMeProfileView

urlpatterns = [path(r"", PrivateMeProfileView.as_view(), name="meapi.profile-details")]
