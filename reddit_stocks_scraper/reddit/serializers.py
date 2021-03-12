#Serializers that conver Django ORM objects into a JSON object for the front end to render
from rest_framework import serializers
from .models import RedditStocksDB

class RedditStocksDBSerializer(serializers.ModelSerializer):
	class Meta:
		model = RedditStocksDB
		fields = "__all__"