# THIS FILE IS THE FUNCTION UTILITY FILE, THIS IS WHERE ALL THE FUNCTIONS ARE DUMPED FOR SCRIPTING SCRAPING PURPOSES


import emojis
import datetime
import time
import threading
import finnhub
import praw
from collections import Counter
from datetime import datetime, date
from scripts.credentials.the_reddit_instance import reddit
from reddit.models import RedditWallStreetBetsStocksDB
#setup zone
# api for stock checking
finnhub_client = finnhub.Client(api_key="c0udc3v48v6r0udvod5g")

#end-setup-zone

def dict_factory (cursor, row):
	""" Funtion for rending fetchall do be in a dictionary"""
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

def get_date(submission):
	""" GETS datetime obj"""
	time = submission.created
	return datetime.fromtimestamp(time)

def get_date_utc(submission):
	date = submission.created_utc
	date_obj = datetime.fromtimestamp(date)
	date_formatted = date_obj.strftime("%x")
	return date_formatted

def get_time_utc(submission):
	time = submission.created_utc
	time_obj = datetime.fromtimestamp(time)
	time_formatted = time_obj.strftime("%X")
	return time_formatted

# removes all $
def cash_tag_remover(dataset : list):
	result_list = list()
	for x in dataset:
		new_x = x[0].replace("$","")
		if new_x != str():
			new_tuple_x = result_list.append((new_x, ))
		if new_x != ')':
			new_tuple_x = result_list.append((new_x, ))
		else:
			continue
	return result_list

#function under construction
def get_individual_unique_cashtag(dataset : list):
	"""GETS all individaul cash tag, returns a list of them"""
	dataset_upper = [i.upper() for i in dataset]
	memory_location = list()
	for item in dataset_upper:
		if not item in memory_location:
			memory_location.append(item)
		else:
			continue
	return memory_location


# note this function is only meant for the original data. fetched from pushift API
def characters_remover(dataset : list):
	""" Removes characters from a list of tuples containing string"""
	def refactoring(x):
		clean = list()
		characters = ["!","@","#","$","%","^","&","*","(",")","-","+","{","}","[","]","/","|",".",",","?",">","<","'",":",";",'"',"~",  "`",]
		global_x = x[0]
		for i in characters:
			if i in global_x:
				global_x = global_x.replace(i,"")

		if global_x != str():
			clean.append((global_x,))
			return clean[0]
		else:
			return x


	no_character_ds = list(map(refactoring, dataset))
	return no_character_ds

#note this is only avaliable from the data originally gotten from push shift API
def extracted_emojis(dataset : list):
	""" Removes any form of emoji"""
	removed_emojis = list()
	reference_dataset = dataset #list
	emojis_symbols = emojis.db.get_emoji_aliases().values()
	for symbol in reference_dataset:
		for emoji in emojis_symbols:
			if emoji in symbol[0]:
				if not (symbol[0],) in removed_emojis:
					removed_emojis.append((symbol[0],))
			else:
				continue
	return removed_emojis

#removes emojis from extracted_emojis
def second_dataset(extracted_emojis : list):
	second_dataset_list = list()
	for data_emoji in extracted_emojis:
		emojis_symbols = list(emojis.db.get_emoji_aliases().values())
		if data_emoji[0][0] in emojis_symbols:
			z = data_emoji[0][0]
			data_emoji[0].replace(z,"")
		decoded = emojis.decode(data_emoji[0])
		index_start = decoded.find(":")
		result = decoded[0:index_start]
		second_dataset_list.append((result,))
	return second_dataset_list


def emoji_remover(dataset:list, emojidataset:list):
	#filter data function for map function
	#x represent dataset
	def no_emoji_filter(x):
		if not x in emojidataset:
			return x
	no_emoji_ds = list(filter(no_emoji_filter, dataset))

	return no_emoji_ds

def merge_dataset(dataset:list , dataset2:list):
	for data in dataset2:
		if data != ('',):
			dataset.append(data)
		else:
			continue
	return dataset

def remove_irregularites(dataset):
	result = list()
	for i in dataset:
		if i[0] != str():
			result.append(i)
		else:
			pass
	return result

def filter_valid_stocks(dataset:list):
	valid_stocks_dataset = list()
	garbage = list()
	def filter_valid_stocks_task(x):
		def check(x):
			criteria = {'s': 'no_data'}
			#make api call to the specified stock
			res = finnhub_client.stock_candles(x, 'D', 1590988249, 1591852249)
			if res != criteria:
				valid_stocks_dataset.append(x)
			else:
				garbage.append(x)
		try:
			check(x)
		except:
			if Exception =="FinnhubAPIException(status_code: 429): API limit reached. Please try again later. Remaining Limit: 0":
				memory = x
				time.sleep(0.001)
				check(x)

	print("[INFO] Checking Validity of stock symbols")
	for stock in dataset:
		thread = threading.Thread(target=filter_valid_stocks_task, args=(stock,))
		thread.start()
		thread.join()
	print("[INFO] Validity check done")
	valid_stocks_dataset_upper = [i.upper() for i in valid_stocks_dataset]
	#once multiprocessing done, adds stockes_mentioned file
	with open("stocks_mentioned.txt","w") as file:
		string = str(valid_stocks_dataset_upper)
		file.write(string)
	return valid_stocks_dataset_upper

#function to shows how many time each stock has been listed
def statisticsCounts(dataset : list):
	""" Returns a dictionay to check how many times each stock is listed"""
	counter = Counter(dataset)
	statistics = dict(counter)
	return statistics


# this function, basically gets the most mentioned in a dict
def getMaxFromStatisticsCounts(dataset:dict):
	""" Get the max from the values of statisticsDict dictionay"""
	values = list(dataset.values())
	maximum_num = max(values)
	print(maximum_num)

	#-------Invert dictionay
	items = list(dataset.items())
	new_dict = dict()
	for x in items:
		new_dict[x[1]] = x[0]
	print("Inverted dictionay")
	print(new_dict)
	#----------END-----------
	result = new_dict[maximum_num]
	return result


def most_frequent(dataset):
	return max(set(dataset), key = dataset.count)

def tuple_remover(dataset:list):
	""" Removes any list containg tuples, and replaces them with string"""
	removed_tuples_dataset = list()
	for tup in dataset:
		removed_tuples_dataset.append(tup[0])
	return removed_tuples_dataset
#this function converts to a list(tuple) so it can be added to db
def unserialize_dict(dateset:dict):
	""" Convert ict info to list of tuples"""
	unserialized_dict = list(dateset.items())
	return unserialized_dict

def update_create_db(dataset:list) -> None:
	def get_current_symbol_state(ticker):
		symbol = RedditWallStreetBetsStocksDB.objects.filter(stock_ticker=ticker)
		if symbol.exists():
			return symbol[0]
		else:
			return None
	for item in dataset:
		ticker_record = get_current_symbol_state(item[0])
		if ticker_record: # Update by adding
			ticker_record.stock_ticker = item[0]
			ticker_record.stock_mentions = ticker_record.stock_mentions + item[1]
			ticker_record.save(update_fields=['stock_ticker', 'stock_mentions'])
		else: # creates a new field if it hasnt
			RedditWallStreetBetsStocksDB.objects.create(stock_ticker=item[0], stock_mentions=item[1])
#-------------FUNCTIONS REGARDING REDDIT CATEGORY SCRAPING--------------

def statistics_hot_data(subreddit:str) -> list :
	""" Function that getts only the hottest threads from reddit"""
	#[{ Title:{User:h, ups:h, downs:h, created_at:h} }]
	statistics_dictionary = dict()
	subreddit = reddit.subreddit(subreddit)
	subreddit_hot = subreddit.hot(limit=None) 

	for submission in subreddit_hot:
		if not submission.stickied:
			title = submission.title
			date_created = get_date_utc(submission)
			time_created = get_time_utc(submission)
			if submission.author is None or submission.author == None:
				print(submission.author, "is none")
				author = submission.author
			else:
				author = submission.author.name
			ups = submission.ups
			comments = submission.num_comments
			upvote_ratio = submission.upvote_ratio
			url = f"https://reddit.com{submission.permalink}"
			statistics_dictionary[title] = {"author" :author, "upvotes":ups, "comments":comments, "upvoteRatio":upvote_ratio, "url":url, "dateCreated":date_created, "timeCreated":time_created}
	return statistics_dictionary

#the following functions are  under testing construction
def statistics_top_data(subreddit:str) -> list :
	""" Function that getts only the Top(Toppest) threads from reddit"""
	#[{ Title:{User:h, ups:h, downs:h, created_at:h} }]
	statistics_dictionary = dict()
	subreddit = reddit.subreddit(subreddit)
	subreddit_top = subreddit.top(limit=None)

	for submission in subreddit_top:
		if not submission.stickied:
			title = submission.title
			date_created = get_date_utc(submission)
			time_created = get_time_utc(submission)
			if submission.author is None or submission.author == None:
				author = submission.author
			else:
				author = submission.author.name
			ups = submission.ups
			comments = submission.num_comments
			upvote_ratio = submission.upvote_ratio
			url = f"https://reddit.com{submission.permalink}"
			statistics_dictionary[title] = {"author" :author, "upvotes":ups, "comments":comments, "upvoteRatio":upvote_ratio, "url":url, "dateCreated":date_created, "timeCreated":time_created}
	return statistics_dictionary

def statistics_new_data(subreddit:str) -> list :
	""" Function that getts only the Top(Toppest) threads from reddit"""
	#[{title:{}}]
	statistics_dictionary = dict()
	subreddit = reddit.subreddit(subreddit)
	subreddit_new = subreddit.new(limit=None)

	for submission in subreddit_new:
		if not submission.stickied:
			title = submission.title
			date_created = get_date_utc(submission)
			time_created = get_time_utc(submission)
			if submission.author is None or submission.author == None:
				print(submission.author, "is none")
				author = submission.author
			else:
				author = submission.author.name
			ups = submission.ups
			comments = submission.num_comments
			upvote_ratio = submission.upvote_ratio
			url = f"https://reddit.com{submission.permalink}"
			statistics_dictionary[title] = {"author" :author, "upvotes":ups, "comments":comments, "upvoteRatio":upvote_ratio, "url":url, "dateCreated":date_created, "timeCreated":time_created}
	return statistics_dictionary


#The below Function is no longer needed, but is here for code referencing
def check_data_in_db(databaseModel, dataset) -> bool:
	""" Checks whether data is present already in database"""
	def unserialize_database_data(x):
		#order = (title, author, upvotes, comments, up_votes_ratio, url, date_created, time_created)
		title 			= x.title
		author 			= x.author
		upvotes 		= x.upvotes
		comments 		= x.comments
		up_votes_ratio 	= x.up_votes_ratio
		url				= x.url
		date_created 	= x.date_created
		time_created	= x.time_created
		unserialized 	= (title, author, upvotes, comments, up_votes_ratio, url, date_created, time_created)
		return unserialized
	def unserialize_dataset_data(t:tuple):
		title  			= t[0]
		author 			= dataset[t[0]]["author"]
		upvotes 		= dataset[t[0]]["upvotes"]
		comments		= dataset[t[0]]["comments"]
		up_votes_ratio	= dataset[t[0]]["upvoteRatio"]
		url				= dataset[t[0]]["url"]
		date_created	= dataset[t[0]]["dateCreated"]
		time_created	= dataset[t[0]]["timeCreated"]
		unserialized	= (title, author, upvotes, comments, up_votes_ratio, url, date_created, time_created)
		return unserialized

	database_data = list(databaseModel.objects.all())
	dataset_data = dataset.items()
	#list of tuples
	unserialized_database_data  = list(map(unserialize_database_data, database_data))
	#list of tuples
	unserialized_dataset_data 	=list(map(unserialize_dataset_data, list(dataset_data)))

	if unserialized_database_data == unserialized_dataset_data:
		print(unserialized_database_data)
		return True
	if unserialized_database_data != unserialized_dataset_data:
		return False
	else:
		return "Something Happened"
