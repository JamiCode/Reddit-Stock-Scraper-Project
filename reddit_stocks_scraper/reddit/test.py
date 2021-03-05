
import finnhub
import time
import threading
from threading import Thread

# Setup client
finnhub_client = finnhub.Client(api_key="c0udc3v48v6r0udvod5g")

# res = finnhub_client.stock_candles('Lop', 'D', 1590988249, 1591852249)
# print(res)
# print(type(res))
supreme = []
def runtask(x):
	def check():
			criteria = {'s': 'no_data'}
			res = finnhub_client.stock_candles(x, 'D', 1590988249, 1591852249)
			if res != criteria:
				print(x,"pass")
				supreme.append(x)
			else:
				pass
	try:
		check()
	except Exception as e:
		if Exception =="FinnhubAPIException(status_code: 429): API limit reached. Please try again later. Remaining Limit: 0":
			time.sleep(0.001)
			check()
stocks = ['350+SHARE', 'NDL', 'BFCH', 'MANU', 'TWO', 'Clsk', 'STTTF', 'Feb', 'SVAC', 'HOT', 'SSY', 'WIN', 'DFLY', 'WINKF', 'DFLYF', 'GMAT', 'ZNGA', 'EN', 'CAN', 'KERN', '17+', '1382', 'VYON', 'SPONF', 'TRMT', '20Gs', 'ABEV', 'NSAV', 'Nimiq', 'HOLL', '270', 'HOFV', 'WLK', 'RĮOT', 'DENT', 'GAME', 'MLLLF', 'BLUE', '30B', '20S', 'FCEL', 'ENG', '200M', '4B', 'NLG', '', 'TDS', 'LIFE', '69M', 'SELB', 'HUTMF', '2700000000', '419', 'PACE', 'BOXL', 'AFRM', '38000', '6999999', 'HTOO', 'EBS', 'BNB', '68', 'Renn', 'NEPT', '999', 'NPA', '110C', 'BIDU', '537', '10What', 'XPEV', 'LHDX', 'BEE', 'DFV', '690', '150000', 'CNDT', 'RXT', '005', 'FUV', 'AmznSq', 'VJET', 'VALE', '300K', '1800', 'TBIO', '44', '600+', 'QMCO', '840', '124', 'BNGO', '4999', 'CCIV&gt;GME', 'APT', '1980', 'BMBL', 'CLF', 'MT', 'RAVENCOIN', 'WSBQ', 'FLTV', 'RAD', 'COMS', 'CORE', 'Delta', 'SWRM', 'RMTD', '318', '10PLUS', 'VSTM', '162', '2+', 'CUEN', '17', 'BP', 'PHAS', 'SGMD', 'BECKY', 'KYLE', '17000', 'GAHC', '1671', '676', 'EOLS', '5800', 'AFPW', 'AKBA', '2750', 'MSNVF', 'CAPA', 'FRX', 'VRA', 'CLIS', '120K+', '9903150', 'DIGICN', '22000', 'ATNF', '700K', '18350', 'SUPV', 'RTLR', '200069', '100200', 'Bbdbca', '3BIL', 'AVLNF', '2571', '50ISH', '210C', '215C', '90C', '275C', '220K', '1387', 'KAR', 'BITF', 'MGTI', 'GMC', 'BANT', 'Pfizer', 'WSGF', '27K', '1G&gt;90G', 'UUP', 'IPIX', 'CBDL', '1548', 'CARV', 'SDE', ]

st = time.time()
for i in stocks:
	print("A new task has started")
	thread = threading.Thread(target=runtask, args=(i,))
	thread.start()
	thread.join()
end = time.time()

print('All done, Took', end, "seconds")
print(supreme)