from django.contrib import admin
from django.urls import path, include
from .views import RedditStocksDBListView
from .views import RedditWallStreetBetsHotAPIView
from .views import RedditWallStreetBetsNewAPIView
from .views import RedditWallStreetBetsTopAPIView

app_name = "reddit"

urlpatterns = [
	path('api/stocks-overall-view-wallstreetbets',
		RedditStocksDBListView.as_view(), name="overall-wallstreetbet-view"),
	path('api/stocks-hot-wallstreetbets', RedditWallStreetBetsHotAPIView.as_view(), name="wallsteetbets-hot"),
	path('api/stocks-new-wallstreetbets', RedditWallStreetBetsNewAPIView.as_view(), name="wallsteetbets-new"),
	path('api/stocks-top-wallstreetbets', RedditWallStreetBetsTopAPIView.as_view(), name="wallsteetbets-top")
	
]
