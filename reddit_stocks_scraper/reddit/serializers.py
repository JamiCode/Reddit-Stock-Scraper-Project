from rest_framework import serializers
from .models import ScrapedStocksStatisticDB

class ScrapedStocksStatisticDBSerializer(serializers.ModelSerializer):

	class Meta:
		model = ScrapedStocksStatisticDB #clone ScrapedStocksB to serializer
		fields = "__all__"

