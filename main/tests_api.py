from TopTrends.schema import Query
from django.test.testcases import TestCase
import graphene

class CountriesTest(TestCase):

    def test_correct_all_countries(self):

        query = """
            query{
                allCountries{
                    id,
                    name,
                    nativeName,
                    acronym,
                    flag,
                    woeid,
                    pn
                } 
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['allCountries']), 250)

class TwitterTrendsTest(TestCase):

    def test_correct_country_defined_trends_number(self):

        query = """
            query{
                countryTwitterTrends(country: "Spain", trendsNumber:10){
                    id,
                    name,
                    url,
                    tweetVolume
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 10)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 10)

    def test_correct_country_undefined_trends_number(self):

        query = """
            query{
                countryTwitterTrends(country: "Spain"){
                    id,
                    name,
                    url,
                    tweetVolume
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 5)

    def test_correct_country_big_trends_number(self):

        query = """
            query{
                countryTwitterTrends(country: "Spain", trendsNumber:500){
                    id,
                    name,
                    url,
                    tweetVolume
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 25)

    def test_unknown_country(self):

        query = """
            query{
                countryTwitterTrends(country: "Not country"){
                    id,
                    name,
                    url,
                    tweetVolume
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 0)

class GoogleTrendsTest(TestCase):

    def test_correct_country_defined_trends_number(self):

        query = """
            query{
                countryGoogleTrends(country:"United States of America", trendsNumber:10){
                    id,
                    name
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 10)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 10)

    def test_correct_country_undefined_trends_number(self):

        query = """
            query{
                countryGoogleTrends(country:"United States of America"){
                    id,
                    name
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 5)

    def test_correct_country_big_trends_number(self):

        query = """
            query{
                countryGoogleTrends(country:"United States of America", trendsNumber:500){
                    id,
                    name
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 20)

    def test_unknown_country(self):

        query = """
            query{
                countryGoogleTrends(country:"Not country"){
                    id,
                    name
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 0)