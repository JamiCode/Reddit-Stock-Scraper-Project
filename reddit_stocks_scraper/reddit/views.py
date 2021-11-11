import threading
import time
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RedditWallStreetBetsStocksDB
from .models import RedditWallStreetBetsHotDB
from .models import RedditWallStreetBetsNewDB
from .models import RedditWallStreetBetsTopDB
from .serializers import RedditWallStreetBetsStocksDBSerializer
from .serializers import RedditWallStreetBetsHotDBSerializer
from .serializers import RedditWallStreetBetsNewDBSerializer
from .serializers import RedditWallStreetBetsTopDBSerializer
# API JSON VIEWS

# view responsible for showing all json of stocks scraped
class RedditStocksDBListView(generics.ListAPIView):
	queryset = RedditWallStreetBetsStocksDB.objects.all()
	serializer_class = RedditWallStreetBetsStocksDBSerializer


# View that is responsible for showing Hot json endpoint

class RedditWallStreetBetsHotAPIView(APIView):
	""" API VIEW Responsible for Hot DB views"""
	def get(self, request, format=None):
		queryset= RedditWallStreetBetsHotDB.objects.all()
		serializer = RedditWallStreetBetsHotDBSerializer(queryset, many=True)
		return Response(serializer.data , status=status.HTTP_200_OK)


class RedditWallStreetBetsNewAPIView(APIView):
	"""API VIEW  Responsible for New DB views"""
	def get(self, request, format=None):
		queryset= RedditWallStreetBetsNewDB.objects.all()
		serializer = RedditWallStreetBetsNewDBSerializer(queryset, many=True)
		return Response(serializer.data , status=status.HTTP_200_OK)

class RedditWallStreetBetsTopAPIView(APIView):
	"""API VIEW  Responsible for New DB views"""
	def get(self, request, format=None):
		queryset= RedditWallStreetBetsTopDB.objects.all()
		serializer = RedditWallStreetBetsTopDBSerializer(queryset, many=True)
		return Response(serializer.data , status=status.HTTP_200_OK)