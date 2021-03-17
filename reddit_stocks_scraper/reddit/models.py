from django.db import models

# Create your models here.
class RedditWallStreetBetsStocksDB(models.Model):
	stock_ticker = models.CharField(max_length=5, unique=True)
	stock_mentions = models.IntegerField()

	def __str__(self):
		return f"{self.stock_ticker} record"

#WallSteetBetsDB Hot Category
class RedditWallStreetBetsHotDB(models.Model):
	title 			= models.TextField()
	author  		= models.CharField(max_length=250, null=True)
	upvotes 		= models.IntegerField()
	comments		= models.IntegerField()
	up_votes_ratio 	= models.DecimalField(max_digits=3, decimal_places=2)
	url 			= models.URLField()
	date_created 	= models.TextField()
	time_created 	= models.TextField()

	def __str__(self):
		return f"{self.title} Hot Record"

#WallSteetBetsDB Top Category
class RedditWallStreetBetsTopDB(models.Model):
	title 			= models.TextField()
	author  		= models.CharField(max_length=250, null=True)
	upvotes 		= models.IntegerField()
	comments		= models.IntegerField()
	up_votes_ratio 	= models.DecimalField(max_digits=3, decimal_places=2)
	url 			= models.URLField()
	date_created 	= models.TextField()
	time_created 	= models.TextField()

	def __str__(self):
		return f"{self.title} Hot Record"


class RedditWallStreetBetsNewDB(models.Model):
	title 			= models.TextField()
	author  		= models.CharField(max_length=250, null=True)
	upvotes 		= models.IntegerField()
	comments		= models.IntegerField()
	up_votes_ratio 	= models.DecimalField(max_digits=3, decimal_places=2)
	url 			= models.URLField()
	date_created 	= models.TextField()
	time_created 	= models.TextField()

	def __str__(self):
		return f"{self.title} Hot Record"	