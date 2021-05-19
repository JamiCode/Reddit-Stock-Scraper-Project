import praw
import time
import asyncio
from .functions.func import *
from .credentials.the_reddit_instance import reddit
from reddit.models import RedditWallStreetBetsHotDB
from reddit.models import RedditWallStreetBetsTopDB
from reddit.models import RedditWallStreetBetsNewDB
class RedditCategories:

	def __init__(self, subreddit):
		#instance variables
		self.subreddit = subreddit
		self.stock_hot_data = None
		self.stock_top_data = None
		self.stock_new_data = None
	# Methods for getting categories
	def get_stats_hot_data(self):
		hot_statistics = statistics_hot_data(self.subreddit)
		self.stock_hot_data = hot_statistics
		return hot_statistics

	def get_stats_top_data(self):
		top_statistics = statistics_top_data(self.subreddit)
		self.stock_top_data = top_statistics
		return top_statistics
	def get_stats_new_data(self):
		new_statistics = statistics_new_data(self.subreddit)
		self.stock_new_data = new_statistics
		return new_statistics



	#END Methods for getting categories

	#START updating/adding to various categories DB
	def update_add_hot_to_db(self):
		""" Updates and add hpt submissions to DB"""
		print(f"[INFO] Watching the Hot category from {self.subreddit}")
		if self.stock_hot_data== None:
			print("[Database Info] Statistic hot category is about to start")

		def unserialize(t:tuple):
			title  			= t[0]	
			author 			= self.stock_hot_data[t[0]]["author"]
			upvotes 		= self.stock_hot_data[t[0]]["upvotes"]
			comments		= self.stock_hot_data[t[0]]["comments"] 
			up_votes_ratio	= self.stock_hot_data[t[0]]["upvoteRatio"] 
			url				= self.stock_hot_data[t[0]]["url"]
			date_created	= self.stock_hot_data[t[0]]["dateCreated"]
			time_created	= self.stock_hot_data[t[0]]["timeCreated"]
			unserialized	= (title, author, upvotes, comments, up_votes_ratio, url, date_created, time_created)
			return unserialized
		def get_current_db_state(title):
			title = RedditWallStreetBetsHotDB.objects.filter(title=title)
			if title.exists():
				return title[0]
			else:
				return None
		unserialized = list(map(unserialize, list(self.stock_hot_data.items())))
		for data in unserialized:
			data_record = get_current_db_state(data[0])
			if data_record:
				# update by changing
				data_record.title 				=	data[0]  			
				data_record.author  			=	data[1]		
				data_record.upvotes 			=	data[2]		
				data_record.comments			=	data[3]		
				data_record.up_votes_ratio		=	data[4] 	
				data_record.url 				=	data[5]
				data_record.date_created 		=	data[6]	
				data_record.time_created 		=	data[7]
				data_record.save()	
			else:
				#Create a record in db
				RedditWallStreetBetsHotDB.objects.create(
						title			=	data[0],
						author			=	data[1],
						upvotes			=	data[2],
						comments		=	data[3],
						up_votes_ratio	=	data[4],
						url				=	data[5],
						date_created	=	data[6],
						time_created	=	data[7],
					)
		print("add/update to DB done")

	def update_add_top_to_db(self):
		""" Updates and adds 'top' submissions threads to DB """
		print(f"[INFO] Watching the Top category from {self.subreddit}")
		if self.stock_hot_data== None:
			print("[Database Info] Statistic top category scraping about to start")

		def unserialize(t:tuple):
			title  			= t[0]	
			author 			= self.stock_top_data[t[0]]["author"]
			upvotes 		= self.stock_top_data[t[0]]["upvotes"]
			comments		= self.stock_top_data[t[0]]["comments"] 
			up_votes_ratio	= self.stock_top_data[t[0]]["upvoteRatio"] 
			url				= self.stock_top_data[t[0]]["url"]
			date_created	= self.stock_top_data[t[0]]["dateCreated"]
			time_created	= self.stock_top_data[t[0]]["timeCreated"]
			unserialized	= (title, author, upvotes, comments, up_votes_ratio, url, date_created, time_created)
			return unserialized
		def get_current_db_state(title):
			title = RedditWallStreetBetsTopDB.objects.filter(title=title)
			if title.exists():
				return title[0]
			else:
				return None
		unserialized = list(map(unserialize, list(self.stock_top_data.items())))
		for data in unserialized:
			data_record = get_current_db_state(data[0])
			if data_record:
				# update by changing
				data_record.title 				=	data[0]  			
				data_record.author  			=	data[1]		
				data_record.upvotes 			=	data[2]		
				data_record.comments			=	data[3]		
				data_record.up_votes_ratio		=	data[4] 	
				data_record.url 				=	data[5]
				data_record.date_created 		=	data[6]	
				data_record.time_created 		=	data[7]
				data_record.save()	
			else:
				#Create a record in db
				RedditWallStreetBetsTopDB.objects.create(
						title			=	data[0],
						author			=	data[1],
						upvotes			=	data[2],
						comments		=	data[3],
						up_votes_ratio	=	data[4],
						url				=	data[5],
						date_created	=	data[6],
						time_created	=	data[7],
					)
		print("add/update to DB done")
	def update_add_new_to_db(self):
		""" Updates and adds 'new' submissions thread to DB"""
		print(f"[INFO] Watching the New category from {self.subreddit}")
		if self.stock_hot_data== None:
			print("[Database Info] Statistic new category scraping has not yet started")

		def unserialize(t:tuple):
			title  			= t[0]	
			author 			= self.stock_new_data[t[0]]["author"]
			upvotes 		= self.stock_new_data[t[0]]["upvotes"]
			comments		= self.stock_new_data[t[0]]["comments"] 
			up_votes_ratio	= self.stock_new_data[t[0]]["upvoteRatio"] 
			url				= self.stock_new_data[t[0]]["url"]
			date_created	= self.stock_new_data[t[0]]["dateCreated"]
			time_created	= self.stock_new_data[t[0]]["timeCreated"]
			unserialized	= (title, author, upvotes, comments, up_votes_ratio, url, date_created, time_created)
			return unserialized
		def get_current_db_state(title):
			title = RedditWallStreetBetsNewDB.objects.filter(title=title)
			if title.exists():
				return title[0]
			else:
				return None
		unserialized = list(map(unserialize, list(self.stock_new_data.items())))
		for data in unserialized:
			data_record = get_current_db_state(data[0])
			if data_record:
				# update by changing
				data_record.title 				=	data[0]  			
				data_record.author  			=	data[1]		
				data_record.upvotes 			=	data[2]		
				data_record.comments			=	data[3]		
				data_record.up_votes_ratio		=	data[4] 	
				data_record.url 				=	data[5]
				data_record.date_created 		=	data[6]	
				data_record.time_created 		=	data[7]	
				data_record.save()
			else:
				#Create a record in db
				RedditWallStreetBetsNewDB.objects.create(
						title			=	data[0],
						author			=	data[1],
						upvotes			=	data[2],
						comments		=	data[3],
						up_votes_ratio	=	data[4],
						url				=	data[5],
						date_created	=	data[6],
						time_created	=	data[7],
					)
		print("add/update to DB done")


def run():
	""" Entry point for runscript"""
	wallstreetbets_category = RedditCategories("wallstreetbets")
	print(f"[INFO] Watching out for {wallstreetbets_category.subreddit} categories")
	wallstreetbets_category.get_stats_hot_data()
	print("[INFO] DONE WITH HOT")
	wallstreetbets_category.get_stats_top_data()
	print("[INFO] DONE WITH TOP")
	wallstreetbets_category.get_stats_new_data()
	print("[INFO] DONE WITH NEW")
	wallstreetbets_category.update_add_hot_to_db()
	wallstreetbets_category.update_add_top_to_db()
	wallstreetbets_category.update_add_new_to_db()
	print("[INFO] Done Updating")



 
