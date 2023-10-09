
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('Superadmin.urls')),
    path('', include('Admins.urls')),
    path('', include('Subadmin.urls')),
    path('', include('Faculty.urls')),
    path('', include('Student.urls')),
    path('', include('Home.urls')),
    path('admin/', admin.site.urls),
]
