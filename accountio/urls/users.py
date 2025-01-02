from django.urls import path
from ..views.users import UserRegisterView, UserListView, UserDetailsView, UserLoginView

urlpatterns = [
    path(r"/login", UserLoginView.as_view(), name="accouintio.users-login"),
    path(r"/register", UserRegisterView.as_view(), name="accouintio.users-register"),
    path(r"/<int:id>", UserDetailsView.as_view(), name="accouintio.users-details"),
    path(r"", UserListView.as_view(), name="accouintio.users-list"),
]
