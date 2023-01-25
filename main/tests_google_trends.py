from django.test import TestCase
from main.models import Country, GoogleTrend, GoogleCountryTrend

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