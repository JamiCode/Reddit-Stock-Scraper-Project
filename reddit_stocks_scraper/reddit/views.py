from django.shortcuts import render
from .serializers import RedditStocksDBSerializer
from .models import RedditStocksDB
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# API JSON VIEWS

# view responsible for showing all json of stocks scraped
class RedditStocksDBListView(generics.ListAPIView):
	queryset = RedditStocksDB.objects.all()
	serializer_class = RedditStocksDBSerializer