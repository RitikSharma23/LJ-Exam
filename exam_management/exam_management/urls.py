from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("home.urls")),
    path("adminpage/", include("adminpage.urls")),
    path("student/", include("student.urls")),
    path("seat/", include("seat.urls")),
    path("marks/", include("marks.urls")),
    path("result/", include("result.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
