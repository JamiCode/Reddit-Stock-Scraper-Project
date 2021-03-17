from django.contrib import admin
from .models import RedditWallStreetBetsStocksDB
from .models import RedditWallStreetBetsHotDB
from .models import RedditWallStreetBetsNewDB
from .models import RedditWallStreetBetsTopDB
# Register your models here.
admin.site.register(RedditWallStreetBetsStocksDB)
admin.site.register(RedditWallStreetBetsHotDB)
admin.site.register(RedditWallStreetBetsNewDB)
admin.site.register(RedditWallStreetBetsTopDB)
