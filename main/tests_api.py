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
