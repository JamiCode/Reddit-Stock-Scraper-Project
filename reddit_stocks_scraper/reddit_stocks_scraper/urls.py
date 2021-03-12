from django.contrib import admin
from django.urls import path, include
from frontend.views import home_view
app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reddit/', include('reddit.urls')),
    path('',home_view)
]
