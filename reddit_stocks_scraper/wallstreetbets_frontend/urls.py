from django.contrib import admin
from django.urls import path, include
from wallstreetbets_frontend.views import index_view
app_name = "wallstreetbets"

urlpatterns = [
    path("",index_view, name="wallstreetbet_index")
]
