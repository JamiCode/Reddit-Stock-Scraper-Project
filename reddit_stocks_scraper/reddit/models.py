from django.db import models

class ScrapedStocksStatisticDB(models.Model):
	stock_ticker = models.CharField(
			max_length=5, 
			unique=True,
			verbose_name="The Stock ticker",
			blank=False
		)
	mentioned_count = models.IntegerField(
			verbose_name="Count",
			blank=False,
			unique=False,
		)

