from django.db import models

# Create your models here.

class Country(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    native_name = models.CharField(max_length=60)
    acronym = models.CharField(max_length=2)
    flag = models.URLField(max_length=100)
    woeid = models.IntegerField(null=True)
    pn = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

class TwitterTrend(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    tweet_volume = models.IntegerField(null=True)
    country_trend = models.ForeignKey('TwitterCountryTrend', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class TwitterCountryTrend(models.Model):

    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country.name

    class Meta:
        ordering = ['country']

class GoogleTrend(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country_trend = models.ForeignKey('GoogleCountryTrend', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class GoogleCountryTrend(models.Model):

    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country.name

    class Meta:
        ordering = ['country']
        
class GoogleWordTrendPeriod(models.Model):
    
    id = models.AutoField(primary_key=True)
    trend_datetime = models.DateTimeField()
    value = models.SmallIntegerField()
    word_trend = models.ForeignKey('GoogleWordTrend', on_delete=models.CASCADE)

    def __str__(self):
        return self.word_trend.country.name + ' - ' + self.word_trend.word + ' - ' + str(self.trend_datetime)

    class Meta:
        ordering = ['word_trend', 'trend_datetime']

class GoogleWordTrend(models.Model):

    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    period_type = models.CharField(max_length=10)

    def __str__(self):
        return self.country.name + ' - ' + self.word

    class Meta:
        ordering = ['country', 'word']

class YouTubeTrend(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    published_at = models.DateTimeField()
    thumbnail = models.URLField(max_length=100)
    channel_title = models.CharField(max_length=100)
    country_trend = models.ForeignKey('YoutubeCountryTrend', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

class YouTubeTrendType(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category_id = models.SmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class YouTubeCountryTrend(models.Model):

    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    trend_type = models.ForeignKey(YouTubeTrendType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.country.name

    class Meta:
        ordering = ['country']