from django.test import TestCase
from main.models import Country, TwitterTrend, TwitterCountryTrend, GoogleTrend, GoogleCountryTrend

FLAG_URL = 'https://flagcdn.com/br.svg'

# Tests from Country model

class CountryModelTest(TestCase):

    def setUp(self):

        Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
    
    ####################################
    ### Country model creation tests ###
    ####################################
    
    def test_correct_country_model_creation(self):

        country = Country.objects.get(woeid=455189)
        self.assertIsNotNone(country)
        
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(country.name, 'Brazil')
        self.assertEqual(country.native_name, 'Brasil')
        self.assertEqual(country.acronym, 'BR')
        self.assertEqual(country.flag, FLAG_URL)
        self.assertEqual(country.woeid, 455189)
        self.assertEqual(country.pn, 'brazil')

    # 'name' field

    def test_correct_country_model_creation_max_length_name(self):
        country = Country.objects.create(name='BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        self.assertEqual(country.name, 'BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazil')

    def test_incorrect_country_model_creation_without_name(self):
        with self.assertRaises(Exception):
            Country.objects.create(name=None, native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')

    def test_incorrect_country_model_creation_blank_name(self):
        with self.assertRaises(Exception):
            country = Country(name='', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_name(self):
        with self.assertRaises(Exception):
            country = Country(name='BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilB', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
            country.full_clean()

    # 'native_name' field

    def test_correct_country_model_creation_max_length_native_name(self):
        country = Country.objects.create(name='Brazil', native_name='BrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        self.assertEqual(country.native_name, 'BrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasil')

    def test_incorrect_country_model_creation_without_native_name(self):
        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name=None, acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')

    def test_incorrect_country_model_creation_blank_native_name(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_native_name(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='BrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasilBrasilB', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
            country.full_clean()

    # 'acronym' field

    def test_incorrect_country_model_creation_without_acronym(self):
        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym=None, flag=FLAG_URL, woeid=455189, pn='brazil')

    def test_incorrect_country_model_creation_blank_acronym(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='', flag=FLAG_URL, woeid=455189, pn='brazil')
            country.full_clean()

    def test_incorrect_country_model_creation_min_length_acronym(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='B', flag=FLAG_URL, woeid=455189, pn='brazil')
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_acronym(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='BRA', flag=FLAG_URL, woeid=455189, pn='brazil')
            country.full_clean()

    # 'flag' field

    def test_correct_country_model_creation_max_length_flag(self):
        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/brbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbr.svg', woeid=455189, pn='brazil')
        self.assertEqual(country.flag, 'https://flagcdn.com/brbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbr.svg')

    def test_incorrect_country_model_creation_without_flag(self):
        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=None, woeid=455189, pn='brazil')
    
    def test_incorrect_country_model_creation_blank_flag(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='BR', flag='', woeid=455189, pn='brazil')
            country.full_clean()

    def test_incorrect_country_model_creation_not_url_flag(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='BR', flag='flag', woeid=455189, pn='brazil')
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_flag(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/brbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrb.svg', woeid=455189, pn='brazil')
            country.full_clean()

    # 'woeid' field

    def test_incorrect_country_model_creation_not_integer_woeid(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid='integer', pn='brazil')
            country.full_clean()

    # 'pn' field

    def test_correct_country_model_creation_max_length_pn(self):
        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazilbrazilbrazilbrazilbrazil')
        self.assertEqual(country.pn, 'brazilbrazilbrazilbrazilbrazil')

    def test_incorrect_country_model_creation_blank_pn(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='')
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_pn(self):
        with self.assertRaises(Exception):
            country = Country(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazilbrazilbrazilbrazilbrazilb')
            country.full_clean()

    ##################################
    ### Country model update tests ###
    ##################################

    def test_correct_country_model_update(self):

        country = Country.objects.get(woeid=455189)
        self.assertIsNotNone(country)
                
        country.name = 'Brasil Update'
        country.native_name = 'Brazil Update'
        country.acronym = 'BU'
        country.flag = 'https://flagcdn.com/bu.svg'
        country.woeid = 123456
        country.pn = 'brazil_update'
        country.save()
        
        self.assertEqual(country.name, 'Brasil Update')
        self.assertEqual(country.native_name, 'Brazil Update')  
        self.assertEqual(country.acronym, 'BU')
        self.assertEqual(country.flag, 'https://flagcdn.com/bu.svg')
        self.assertEqual(country.woeid, 123456)
        self.assertEqual(country.pn, 'brazil_update')

    # 'name' field

    def test_correct_country_model_update_max_length_name(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.name = 'BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazil'

        self.assertEqual(country.name, 'BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazil')

    def test_incorrect_country_model_update_without_name(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.name = None
        
        with self.assertRaises(Exception):
            country.full_clean()   

    def test_incorrect_country_model_update_blank_name(self):
            
        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.name = ''
        
        with self.assertRaises(Exception):
            country.full_clean() 

    def test_incorrect_country_model_update_max_length_name(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.name = 'BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilB'
        
        with self.assertRaises(Exception):
            country.full_clean() 

    # 'native_name' field

    def test_correct_country_model_update_max_length_native_name(self):
            
        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.native_name = 'BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazil'
        
        self.assertEqual(country.native_name, 'BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazil')

    def test_incorrect_country_model_update_without_native_name(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.native_name = None
        
        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_blank_native_name(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.native_name = ''
        
        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_max_length_native_name(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.native_name = 'BrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilBrazilB'
        
        with self.assertRaises(Exception):
            country.full_clean()

    # 'acronym' field

    def test_incorrect_country_model_update_without_acronym(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.acronym = None
        
        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_blank_acronym(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.acronym = ''
        
        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_min_length_acronym(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.acronym = 'B'
        
        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_max_length_acronym(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.acronym = 'BRA'
        
        with self.assertRaises(Exception):
            country.full_clean()

    # 'flag' field

    def test_correct_country_model_update_max_length_flag(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.flag = 'https://flagcdn.com/brbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbr.svg'
        
        self.assertEqual(country.flag, 'https://flagcdn.com/brbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbr.svg')

    def test_incorrect_country_model_update_without_flag(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.flag = None
        
        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_blank_flag(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.flag = ''
        
        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_not_url_flag(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.flag = 'flag'
        
        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_max_length_flag(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.flag = 'https://flagcdn.com/brbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrb.svg'
        
        with self.assertRaises(Exception):
            country.full_clean()

    # 'woeid' field

    def test_incorrect_country_model_update_not_integer_woeid(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.woeid = 'integer'

        with self.assertRaises(Exception):
            country.full_clean()

    # 'pn' field

    def test_correct_country_model_update_max_length_pn(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.pn = 'brazilbrazilbrazilbrazilbrazil'

        self.assertEqual(country.pn, 'brazilbrazilbrazilbrazilbrazil')

    def test_incorrect_country_model_update_blank_pn(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.pn = ''

        with self.assertRaises(Exception):
            country.full_clean()

    def test_incorrect_country_model_update_max_length_pn(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil')
        country.pn = 'brazilbrazilbrazilbrazilbrazilbrazilb'

        with self.assertRaises(Exception):
            country.full_clean()

    ##################################
    ### Country model delete tests ###
    ##################################

    def test_correct_country_model_delete(self):
                
        self.assertEqual(Country.objects.count(), 1)

        country = Country.objects.get(woeid=455189)

        self.assertIsNotNone(country)

        country.delete()
        
        self.assertEqual(Country.objects.count(), 0)

    