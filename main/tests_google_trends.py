from django.test import TestCase
from main.models import Country, GoogleTrend, GoogleCountryTrend, GoogleWordTrendPeriod, GoogleWordTrend
from datetime import datetime
import pytz 

# Tests of the Google Trends models

class GoogleTrendsTestCase(TestCase):

    def setUp(self):
        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/br.svg', woeid=455189, pn='brazil')
        self.google_country_trend = GoogleCountryTrend.objects.create(country=country)
        self.google_trend = GoogleTrend.objects.create(name='Trend', country_trend=self.google_country_trend)

    ########################################
    ### GoogleTrend model creation tests ###
    ########################################

    def test_correct_google_trend_model_creation(self):
        
        self.assertEqual(GoogleTrend.objects.count(), 1)
        self.assertEqual(self.google_trend.name, 'Trend')
        self.assertEqual(self.google_trend.country_trend, self.google_country_trend)
        self.assertTrue(isinstance(self.google_trend, GoogleTrend))
        self.assertEqual(self.google_trend.__str__(), self.google_trend.name)

    # 'name' field

    def test_correct_google_trend_model_creation_max_length_name(self):
        google_trend = GoogleTrend.objects.create(name='T'*100, country_trend=self.google_country_trend)
        self.assertEqual(google_trend.name, 'T'*100)

    def test_incorrect_google_trend_model_creation_without_name(self):
        with self.assertRaises(Exception):
            GoogleTrend.objects.create(name=None, country_trend=self.google_country_trend)

    def test_incorrect_google_trend_model_creation_blank_name(self):
        with self.assertRaises(Exception):
            google_trend = GoogleTrend(name='', country_trend=self.google_country_trend)
            google_trend.full_clean()

    def test_incorrect_google_trend_model_creation_max_length_name(self):
        with self.assertRaises(Exception):
            GoogleTrend.objects.create(name='T'*101, country_trend=self.google_country_trend)

    # 'country_trend' field

    def test_incorrect_google_trend_model_creation_without_country_trend(self):
        with self.assertRaises(Exception):
            GoogleTrend.objects.create(name='Trend', country_trend=None)


    #######################################
    ### GoogleTrend model update tests ####
    #######################################

    def test_correct_google_trend_model_update(self):

        country = Country.objects.create(name='Argentina', native_name='Argentina', acronym='AR', flag='https://flagcdn.com/ar.svg', woeid=332471, pn='argentina')
        google_country_trend = GoogleCountryTrend.objects.create(country=country)

        self.google_trend.name = 'New Trend'
        self.google_trend.country_trend = google_country_trend
        self.google_trend.save()

        self.assertEqual(GoogleTrend.objects.count(), 1)
        self.assertEqual(self.google_trend.name, 'New Trend')
        self.assertEqual(self.google_trend.country_trend, google_country_trend)

    # 'name' field

    def test_correct_google_trend_model_update_max_length_name(self):
        
        self.google_trend.name = 'T'*100
        self.google_trend.save()
        self.assertEqual(self.google_trend.name, 'T'*100)

    def test_incorrect_google_trend_model_update_without_name(self):
        with self.assertRaises(Exception):
            self.google_trend.name = None
            self.google_trend.save()

    def test_incorrect_google_trend_model_update_blank_name(self):
        with self.assertRaises(Exception):
            self.google_trend.name = ''
            self.google_trend.full_clean()

    def test_incorrect_google_trend_model_update_max_length_name(self):
        with self.assertRaises(Exception):
            self.google_trend.name = 'T'*101
            self.google_trend.save()

    # 'country_trend' field

    def test_incorrect_google_trend_model_update_without_country_trend(self):
        with self.assertRaises(Exception):
            self.google_trend.country_trend = None
            self.google_trend.save()

    #######################################
    ### GoogleTrend model delete tests ####
    #######################################

    def test_correct_google_trend_model_delete(self):

        self.assertEqual(GoogleTrend.objects.count(), 1)
        self.google_trend.delete()
        self.assertEqual(GoogleTrend.objects.count(), 0)

class GoogleCountryTrendModelTestCase(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/br.svg', woeid=455189, pn='brazil')
        self.google_country_trend = GoogleCountryTrend.objects.create(country=self.country)
        self.google_trend = GoogleTrend.objects.create(name='Trend', country_trend=self.google_country_trend)


    ###############################################
    ### GoogleCountryTrend model creation tests ###
    ###############################################

    def test_correct_google_country_trend_model_creation(self):

        self.assertEqual(GoogleCountryTrend.objects.count(), 1)
        self.assertEqual(self.google_country_trend.country, self.country)
        self.assertTrue(isinstance(self.google_country_trend, GoogleCountryTrend))
        self.assertEqual(self.google_country_trend.__str__(), self.country.name)

    # 'country' field

    def test_incorrect_google_country_trend_model_creation_without_country(self):
        with self.assertRaises(Exception):
            GoogleCountryTrend.objects.create(country=None)

    ##############################################
    ### GoogleCountryTrend model update tests ###
    ##############################################

    def test_correct_google_country_trend_model_update(self):

        country = Country.objects.create(name='Argentina', native_name='Argentina', acronym='AR', flag='https://flagcdn.com/ar.svg', woeid=332471, pn='argentina')

        self.google_country_trend.country = country
        self.google_country_trend.save()

        self.assertEqual(GoogleCountryTrend.objects.count(), 1)
        self.assertEqual(self.google_country_trend.country, country)

    # 'country' field

    def test_incorrect_google_country_trend_model_update_without_country(self):
        with self.assertRaises(Exception):
            self.google_country_trend.country = None
            self.google_country_trend.save()

    ##############################################
    ### GoogleCountryTrend model delete tests ###
    ##############################################

    def test_correct_google_country_trend_model_delete(self):

        self.assertEqual(GoogleCountryTrend.objects.count(), 1)
        self.assertEqual(GoogleTrend.objects.count(), 1)
        self.google_country_trend.delete()
        self.assertEqual(GoogleCountryTrend.objects.count(), 0)
        self.assertEqual(GoogleTrend.objects.count(), 0)

class GoogleWordTrendPeriodModelTestCase(TestCase):

    def setUp(self):
        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/br.svg', woeid=455189, pn='brazil')
        self.google_word_trend = GoogleWordTrend.objects.create(word='Word', country=country, period_type='weekly')
        self.google_word_trend_period = GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=1, word_trend=self.google_word_trend)

    ##################################################
    ### GoogleWordTrendPeriod model creation tests ###
    ##################################################

    def test_correct_google_word_trend_period_model_creation(self):

        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 1)
        self.assertEqual(self.google_word_trend_period.trend_datetime, datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC))
        self.assertEqual(self.google_word_trend_period.value, 1)
        self.assertEqual(self.google_word_trend_period.word_trend, self.google_word_trend)
        self.assertTrue(isinstance(self.google_word_trend_period, GoogleWordTrendPeriod))
        self.assertEqual(self.google_word_trend_period.__str__(), self.google_word_trend.country.name + ' - ' + self.google_word_trend.word + ' - ' + str(self.google_word_trend_period.trend_datetime))

    # 'trend_datetime' field

    def test_incorrect_google_word_trend_period_model_creation_without_trend_datetime(self):
        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=None, value=1, word_trend=self.google_word_trend)
    
    def test_incorrect_google_country_trend_model_creation_not_datetime_trend_datetime(self):
        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime='not_datetime', value=1, word_trend=self.google_word_trend)

    # 'value' field

    def test_correct_google_country_trend_model_creation_not_small_integer_value(self):
        google_word_trend_period = GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=32767, word_trend=self.google_word_trend)
        self.assertEqual(google_word_trend_period.value, 32767)

    def test_incorrect_google_word_trend_period_model_creation_without_value(self):
        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=None, word_trend=self.google_word_trend)

    def test_incorrect_google_country_trend_model_creation_not_integer_value(self):
        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value='not_integer', word_trend=self.google_word_trend)

    def test_incorrect_google_country_trend_model_creation_not_small_integer_value(self):
        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=32768, word_trend=self.google_word_trend)

    # 'word_trend' field

    def test_incorrect_google_word_trend_period_model_creation_without_word_trend(self):
        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=1, word_trend=None)

    ################################################
    ### GoogleWordTrendPeriod model update tests ###
    ################################################

    def test_correct_google_word_trend_period_model_update(self):

        country = Country.objects.create(name='Argentina', native_name='Argentina', acronym='AR', flag='https://flagcdn.com/ar.svg', woeid=332471, pn='argentina')
        google_word_trend = GoogleWordTrend.objects.create(word='Word', country=country, period_type='weekly')

        self.google_word_trend_period.trend_datetime = datetime(2023, 1, 24, 0, 0, 0, 0, pytz.UTC)
        self.google_word_trend_period.value = 21
        self.google_word_trend_period.word_trend = google_word_trend
        self.google_word_trend_period.save()

        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 1)
        self.assertEqual(self.google_word_trend_period.trend_datetime, datetime(2023, 1, 24, 0, 0, 0, 0, pytz.UTC))
        self.assertEqual(self.google_word_trend_period.value, 21)
        self.assertEqual(self.google_word_trend_period.word_trend, google_word_trend)

    # 'trend_datetime' field

    def test_incorrect_google_word_trend_period_model_update_without_trend_datetime(self):
        with self.assertRaises(Exception):
            self.google_word_trend_period.trend_datetime = None
            self.google_word_trend_period.save()
        
    def test_incorrect_google_word_trend_period_model_update_not_datetime_trend_datetime(self):
        with self.assertRaises(Exception):
            self.google_word_trend_period.trend_datetime = 'not_datetime'
            self.google_word_trend_period.save()

    # 'value' field

    def test_correct_google_country_trend_model_update_not_small_integer_value(self):
        self.google_word_trend_period.value = 32767
        self.google_word_trend_period.save()
        self.assertEqual(self.google_word_trend_period.value, 32767)

    def test_incorrect_google_word_trend_period_model_update_without_value(self):
        with self.assertRaises(Exception):
            self.google_word_trend_period.value = None
            self.google_word_trend_period.save()

    def test_incorrect_google_word_trend_period_model_update_not_integer_value(self):
        with self.assertRaises(Exception):
            self.google_word_trend_period.value = 'not_integer'
            self.google_word_trend_period.save()

    def test_incorrect_google_country_trend_model_update_not_small_integer_value(self):
        with self.assertRaises(Exception):
            self.google_word_trend_period.value = 32768
            self.google_word_trend_period.save()

    # 'word_trend' field

    def test_incorrect_google_word_trend_period_model_update_not_word_trend(self):
        with self.assertRaises(Exception):
            self.google_word_trend_period.word_trend = 'not_word_trend'
            self.google_word_trend_period.save()

    ################################################
    ### GoogleWordTrendPeriod model delete tests ###
    ################################################

    def test_correct_google_word_trend_period_model_delete(self):

        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 1)
        self.google_word_trend_period.delete()
        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 0)