import time
import datetime
import emojis
import time
from psaw import PushshiftAPI
from reddit.functions.func import get_date
from reddit.functions.func import dict_factory, get_individual_unique_cashtag
from reddit.functions.func import statisticsCounts
from reddit.functions.func import getMaxFromStatisticsCounts, cash_tag_remover
from reddit.functions.func import characters_remover, most_frequent, extracted_emojis, emoji_remover, second_dataset, merge_dataset, remove_irregularites, tuple_remover, filter_valid_stocks, unserialize_dict
from datetime import datetime, date
# from .models import ScrapedStocksStatisticDB



class Reddit:
	#Class Variables
	global api
	global thumbsup
	global cross
	api = PushshiftAPI() 
	thumbsup = emojis.encode(":thumbsup:")
	cross = emojis.encode(":x:")

	def __init__(self,  subreddit:str):
		print("The Instance has been created")
		self.subreddit = subreddit
		self.stock_mentioned_yesterday = "Scraping did not start yet"
		self.stock_mentioned_default = "Scraping did not start yet"
		self.statistic_count = "Scraping did not start yet"
	
	def begin_scrape_for_yesterday(self):
		""" This method would scrape reddit stocks from wallstreetbets for the previous day once it hits 3am UTC"""
		def get_scrape_time():
			"""GETS scrape time"""
			year = datetime.utcnow().year
			month = datetime.utcnow().month
			day = datetime.utcnow().day
			search_day = day - 1
			start_date_scrape = datetime(year, month, day)
			start_time = int(start_date_scrape.timestamp())
			return start_time
		def scrape_stocks():
			start_time = get_scrape_time()
			submissions = list(api.search_submissions(after=start_time,
		                            subreddit= self.subreddit,
		                            filter=['url','author', 'title', 'subreddit']
		                            ))
			#memory management
			cashtags_list_data = list()
			cashtags_list_data_with_date = list()
			for submission in submissions:
				words = submission.title.split()
				# filter out words, that is a lower and starts with $
				cashtags = tuple(set(filter(lambda word: word.lower().startswith("$"), words))) 
				# if it has any cashtags
				if len(cashtags) > 0:
					mini_cashtags_data = list()
					for i in cashtags:
						mini_cashtags_data.append((i,))
						cashtags_list_data_with_date.append((i,get_date(submission)))
					for n in mini_cashtags_data:
						cashtags_list_data.append(n)
            #--------------------------------------			
			emojis_extracted = extracted_emojis(characters_remover(cash_tag_remover(cashtags_list_data)))
			stc_withem = cash_tag_remover(cashtags_list_data)
			tickers_em = characters_remover(stc_withem)
			stc1 = emoji_remover(tickers_em, emojis_extracted)
			stc2 = second_dataset(emojis_extracted)
			stc_with_tuples= merge_dataset(stc1, stc2)
			#Dealing with no tuples
			stc = tuple_remover(stc_with_tuples) #not a tuple
			stcs_valid = filter_valid_stocks(stc)#not a tuple

			#not a tup
			self.stock_mentioned_yesterday= get_individual_unique_cashtag(stcs_valid)
			self.statistic_count = statisticsCounts(stcs_valid)
			# max_ = getMaxFromStatisticsCounts(stats)
			# mostfreq = most_frequent(stcs_valid)
			return stcs_valid
		
		while True:
			# if the time is 3am, start scraping for yesterday		
			if datetime.utcnow().hour == 4:
				print("Beginning to Scrape for the day")
				start_time = time.time()
				print("[INFO] Scraping Data ......")
				stocks = scrape_stocks()
				end_time = time.time() - start_time
				print(f"[INFO] Done Scraping {thumbsup}| Took {end_time} seconds")
				print("[INFO] CONFIRMING STOCKS")
				with open("stocks_mentioned.txt","r") as file:
					content = file.read()
					str_stocks = str(stocks)
					if str_stocks == content:
						print(f"[INFO] Confirmed Successfully {thumbsup}")
					else:
						print(f"[INFO]{cross} Not Confirmed, using Backup")
				return stocks
				break
			else:
				continue
	
	def begin_scrape_from_default(self):
		""" METHOD that begins scrape from the default, Feb 15"""
		def scrape_stocks():
			start_time = datetime(2021, 2, 15)
			end_time = datetime(2021, 3, 2)
			boolean = isinstance(end_time, datetime)
			submissions = list(api.search_submissions(after=start_time,
		                            subreddit= self.subreddit,
		                            filter=['url','author', 'title', 'subreddit'],
		                            stop_condition=boolean
		                            ))
			#memory management
			cashtags_list_data = list()
			cashtags_list_data_with_date = list()
			for submission in submissions:
				words = submission.title.split()
				# filter out words, that is a lower and starts with $
				cashtags = tuple(set(filter(lambda word: word.lower().startswith("$"), words))) 
				# if it has any cashtags
				if len(cashtags) > 0:
					mini_cashtags_data = list()
					for i in cashtags:
						mini_cashtags_data.append((i,))
						cashtags_list_data_with_date.append((i,get_date(submission)))
					for n in mini_cashtags_data:
						cashtags_list_data.append(n)
            #--------------------------------------			
			emojis_extracted = extracted_emojis(characters_remover(cash_tag_remover(cashtags_list_data)))
			stc_withem = cash_tag_remover(cashtags_list_data)
			tickers_em = characters_remover(stc_withem)
			stc1 = emoji_remover(tickers_em, emojis_extracted)
			stc2 = second_dataset(emojis_extracted)
			stc_with_tuples= merge_dataset(stc1, stc2)
			#Dealing with no tuples
			stc = tuple_remover(stc_with_tuples) #not a tuple
			stcs_valid = filter_valid_stocks(stc)#not a tuple
			#not a tuple
			self.stock_mentioned_default = get_individual_unique_cashtag(stcs_valid)
			self.statistic_count = statisticsCounts(stcs_valid)
			# max_ = getMaxFromStatisticsCounts(stats)
			# mostfreq = most_frequent(stcs_valid)
			return stcs_valid
		

		# starts to	scrape
		if True:
			print("Beginning to Scrape for the day")
			start_time = time.time()
			print("[INFO] Scraping Data ......")
			stocks = scrape_stocks()
			end_time = time.time() - start_time
			print(f"[INFO] Done Scraping {thumbsup}| Took {end_time} seconds")
			return stocks
		else:
			pass



# wall_street_bets = Reddit("wallstreetbets")
# wall_street_bets.begin_scrape_for_yesterday()
# satistics = wall_street_bets.statistic_count
# print("These are the stocks mentions")
# print(wall_street_bets.stock_mentioned_yesterday)
# print(wall_street_bets.statistic_count)
# print(unserialize_dict(wall_street_bets.statistic_count))

