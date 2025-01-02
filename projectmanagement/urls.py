import os

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


# Change Admin Top Nav Header
admin.site.site_header = "Project management tool"

urlpatterns = [
    # Swagger
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path('admin/', admin.site.urls),
    # User related endpoints
    path('api/v1/users', include("accountio.urls")),
    # My all endpoints 
    path('api/v1/me', include("meapi.urls")),
    # Private proejct related all endpoints 
    path('api/v1/projects', include("meapi.urls.projects")),
    # Private task related all endpoints 
    path('api/v1/tasks', include("meapi.urls.tasks")),
]

if os.environ.get("DEBUG") == "True":
    urlpatterns += [path("profiling", include("silk.urls", namespace="silk"))] # Profiling
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

