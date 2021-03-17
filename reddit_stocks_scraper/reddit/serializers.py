#Serializers that conver Django ORM objects into a JSON object for the front end to render
from rest_framework import serializers
from .models import RedditWallStreetBetsStocksDB
from .models import RedditWallStreetBetsHotDB
from .models import RedditWallStreetBetsNewDB
from .models import RedditWallStreetBetsTopDB


class RedditWallStreetBetsStocksDBSerializer(serializers.ModelSerializer):
	class Meta:
		model = RedditWallStreetBetsStocksDB
		fields = "__all__"

class RedditWallStreetBetsHotDBSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = RedditWallStreetBetsHotDB
		fields = "__all__"


class RedditWallStreetBetsNewDBSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = RedditWallStreetBetsNewDB
		fields = "__all__"

class RedditWallStreetBetsTopDBSerializer(serializers.ModelSerializer):
	""" RedditWallStreetBetsTopDB serializers """
	class Meta:
		model = RedditWallStreetBetsTopDB
		fields = "__all__"