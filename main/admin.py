from django.contrib import admin
from main.models import Country, TwitterTrend, TwitterCountryTrend, GoogleTrend, GoogleCountryTrend

# Register your models here.

admin.site.register(Country)
admin.site.register(TwitterTrend)
admin.site.register(TwitterCountryTrend)
admin.site.register(GoogleTrend)
admin.site.register(GoogleCountryTrend)