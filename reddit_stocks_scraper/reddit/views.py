from django.shortcuts import render
from django.http import HttpResponse
from .serializers import ScrapedStocksStatisticDBSerializer
from .models import ScrapedStocksStatisticDB
from .reddit import Reddit

wall_street_bets = Reddit("wallstreetbets")
wall_street_bets.begin_scrape_for_yesterday()
satistics = wall_street_bets.statistic_count
mentioned_yesterday = wall_street_bets.stock_mentioned_yesterday
stats = wall_street_bets.statistic_count
# print("These are the stocks mentions")
# print(wall_street_bets.stock_mentioned_yesterday)
# print(wall_street_bets.statistic_count)
# print(unserialize_dict(wall_street_bets.statistic_count))
# #----------------API VIEWS------------------------ 
def home_view(request):
	return HttpResponse(f"{wall_street_bets.statistic_count}")