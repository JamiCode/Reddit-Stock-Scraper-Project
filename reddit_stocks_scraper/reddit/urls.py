from django.contrib import admin
from django.urls import path, include
from .views import RedditStocksDBListView

app_name = "reddit"

urlpatterns = [
	path('api/stocks-overall-view-wallstreetbets',
		RedditStocksDBListView.as_view(), name="overall-wallstreetbet-view")
]
