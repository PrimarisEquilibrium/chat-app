from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('base.urls')),

    # User Authentication Routes
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
]
