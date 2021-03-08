from django.db import models

# Create your models here.
class RedditStocksDB(models.Model):
	stock_ticker = models.TextField(max_length=5, unique=True)
	stock_mentions = models.IntegerField()

	def __str__(self):
		return f"{self.stock_ticker} record"
