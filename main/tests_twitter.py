from django.test import TestCase
from main.models import Country, TwitterTrend, TwitterCountryTrend

# Tests from Twitter model

class TwitterTrendModelTest(TestCase):

    def setUp(self):
        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/br.svg', woeid=455189, pn='brazil')
        self.twitter_country_trend = TwitterCountryTrend.objects.create(country=country)
        self.twitter_trend = TwitterTrend.objects.create(name='Trend', url='https://trend.com', tweet_volume=100, country_trend=self.twitter_country_trend)

    #########################################
    ### TwitterTrend model creation tests ###
    #########################################

    def test_correct_twitter_trend_model_creation(self):
        
        self.assertEqual(TwitterTrend.objects.count(), 1)
        self.assertEqual(self.twitter_trend.name, 'Trend')
        self.assertEqual(self.twitter_trend.url, 'https://trend.com')
        self.assertEqual(self.twitter_trend.tweet_volume, 100)
        self.assertTrue(isinstance(self.twitter_trend, TwitterTrend))
        self.assertEqual(self.twitter_trend.__str__(), self.twitter_trend.name)

    # 'name' field

    def test_correct_twitter_trend_model_creation_max_length_name(self):
        twitter_trend = TwitterTrend.objects.create(name='TrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrend', url='https://trend.com', tweet_volume=100, country_trend=self.twitter_country_trend)
        self.assertEqual(twitter_trend.name, 'TrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrend')

    def test_incorrect_twitter_trend_model_creation_without_name(self):
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name=None, url='https://trend.com', tweet_volume=100, country_trend=self.twitter_country_trend)

    def test_incorrect_twitter_trend_model_creation_blank_name(self):
        with self.assertRaises(Exception):
            twitter_trend = TwitterTrend(name='', url='https://trend.com', tweet_volume=100, country_trend=self.twitter_country_trend)
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_creation_max_length_name(self):
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='TrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendT', url='https://trend.com', tweet_volume=100, country_trend=self.twitter_country_trend)

    # 'url' field

    def test_correct_twitter_trend_model_creation_max_length_url(self):
        twitter_trend = TwitterTrend.objects.create(name='Trend', url='https://trendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtre.com', tweet_volume=100, country_trend=self.twitter_country_trend)
        self.assertEqual(twitter_trend.url, 'https://trendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtre.com')

    def test_incorrect_twitter_trend_model_creation_without_url(self):
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='Trend', url=None, tweet_volume=100, country_trend=self.twitter_country_trend)

    def test_incorrect_twitter_trend_model_creation_blank_url(self):
        with self.assertRaises(Exception):
            twitter_trend = TwitterTrend(name='Trend', url='', tweet_volume=100, country_trend=self.twitter_country_trend)
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_creation_invalid_url(self):
        with self.assertRaises(Exception):
            twitter_trend = TwitterTrend(name='Trend', url='not_url', tweet_volume=100, country_trend=self.twitter_country_trend)
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_creation_max_length_url(self):
        with self.assertRaises(Exception):
            twitter_trend = TwitterTrend(name='Trend', url='https://trendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtren.com', tweet_volume=100, country_trend=self.twitter_country_trend)
            twitter_trend.full_clean()

    # 'tweet_volume' field

    def test_incorrect_twitter_trend_model_creation_not_integer_tweet_volume(self):
        with self.assertRaises(Exception):
            twitter_trend = TwitterTrend(name='Trend', url='https://trend.com', tweet_volume='not_integer', country_trend=self.twitter_country_trend)
            twitter_trend.full_clean()

    # 'country_trend' field

    def test_incorrect_twitter_trend_model_creation_without_country_trend(self):
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='Trend', url='https://trend.com', tweet_volume=100, country_trend=None)


    #########################################
    ### TwitterTrend model creation tests ###
    #########################################

    def test_correct_twitter_trend_model_update(self):

        self.twitter_trend.name = 'TrendTrend'
        self.twitter_trend.url = 'https://trendtrend.com'
        self.twitter_trend.tweet_volume = 200
        self.twitter_trend.save()

        self.assertEqual(self.twitter_trend.name, 'TrendTrend')
        self.assertEqual(self.twitter_trend.url, 'https://trendtrend.com')
        self.assertEqual(self.twitter_trend.tweet_volume, 200)

    # 'name' field

    def test_correct_country_model_update_max_length_name(self):
        twitter_trend = self.twitter_trend
        twitter_trend.name = 'TrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrend'
        twitter_trend.save()

        self.assertEqual(twitter_trend.name, 'TrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrend')

    def test_incorrect_twitter_trend_model_update_without_name(self):
        
        twitter_trend = self.twitter_trend
        twitter_trend.name = None

        with self.assertRaises(Exception):
            twitter_trend.full_clean()    

    def test_incorrect_twitter_trend_model_update_blank_name(self):

        twitter_trend = self.twitter_trend
        twitter_trend.name = ''

        with self.assertRaises(Exception):
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_update_max_length_name(self):

        twitter_trend = self.twitter_trend
        twitter_trend.name = 'TrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendTrendT'

        with self.assertRaises(Exception):
            twitter_trend.full_clean()

    # 'url' field

    def test_correct_twitter_trend_model_update_max_length_url(self):

        twitter_trend = self.twitter_trend
        twitter_trend.url = 'https://trendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtre.com'
        twitter_trend.save()

        self.assertEqual(twitter_trend.url, 'https://trendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtre.com')

    def test_incorrect_twitter_trend_model_update_without_url(self):
            
        twitter_trend = self.twitter_trend
        twitter_trend.url = None

        with self.assertRaises(Exception):
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_update_blank_url(self):

        twitter_trend = self.twitter_trend
        twitter_trend.url = ''

        with self.assertRaises(Exception):
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_update_invalid_url(self):
        
        twitter_trend = self.twitter_trend
        twitter_trend.url = 'not_url'

        with self.assertRaises(Exception):
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_update_max_length_url(self):

        twitter_trend = self.twitter_trend
        twitter_trend.url = 'https://trendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtrendtren.com'

        with self.assertRaises(Exception):
            twitter_trend.full_clean()

    # 'tweet_volume' field

    def test_incorrect_twitter_trend_model_update_not_integer_tweet_volume(self):
            
        twitter_trend = self.twitter_trend
        twitter_trend.tweet_volume = 'not_integer'

        with self.assertRaises(Exception):
            twitter_trend.full_clean()

    # 'country_trend' field

    def test_incorrect_twitter_trend_model_update_without_country_trend(self):

        twitter_trend = self.twitter_trend
        twitter_trend.country_trend = None

        with self.assertRaises(Exception):
            twitter_trend.full_clean()

    #######################################
    ### TwitterTrend model delete tests ###
    #######################################

    def test_correct_twitter_trend_model_delete(self):

        self.assertEqual(TwitterTrend.objects.count(), 1)

        self.twitter_trend.delete()

        self.assertEqual(TwitterTrend.objects.count(), 0)