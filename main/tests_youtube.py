from django.test import TestCase
from main.models import Country, YouTubeTrendType

# Tests of the YouTube models

class YouTubeTrendTypeTestCase(TestCase):

    def setUp(self):
        self.yt_trend_type = YouTubeTrendType.objects.create(name='Music', category_id=10)

    #############################################
    ### YouTubeTrendType model creation tests ###
    #############################################

    def test_correct_yt_trend_type_model_creation(self):

        self.assertEqual(YouTubeTrendType.objects.count(), 1)
        self.assertEqual(self.yt_trend_type.name, 'Music')
        self.assertEqual(self.yt_trend_type.category_id, 10)
        self.assertTrue(isinstance(self.yt_trend_type, YouTubeTrendType))
        self.assertEqual(self.yt_trend_type.__str__(), self.yt_trend_type.name)

    # 'name' field

    def test_correct_yt_trend_type_model_max_length_name(self):
        yt_trend_type = YouTubeTrendType.objects.create(name='N' * 100, category_id=10)
        self.assertEqual(yt_trend_type.name, 'N'*100)

    def test_incorrect_yt_trend_type_model_without_name(self):
        with self.assertRaises(Exception):
            YouTubeTrendType.objects.create(name=None, category_id=10)

    def test_incorrect_yt_trend_type_model_blank_name(self):
        with self.assertRaises(Exception):
            yt_trend_type = YouTubeTrendType.objects.create(name='', category_id=10)
            yt_trend_type.full_clean()

    def test_incorrect_yt_trend_type_model_max_length_name(self):
        with self.assertRaises(Exception):
            YouTubeTrendType.objects.create(name='N' * 101, category_id=10)

    # 'category_id' field

    def test_correct_yt_trend_type_model_max_integer_category_id(self):
        yt_trend_type = YouTubeTrendType.objects.create(name='Music', category_id=32767)
        self.assertEqual(yt_trend_type.category_id, 32767)

    def test_incorrect_yt_trend_type_model_without_category_id(self):
        with self.assertRaises(Exception):
            YouTubeTrendType.objects.create(name='Music', category_id=None)

    def test_incorrect_yt_trend_type_model_not_integer_category_id(self):
        with self.assertRaises(Exception):
            YouTubeTrendType.objects.create(name='Music', category_id='not_integer')

    def test_incorrect_yt_trend_type_model_max_integer_category_id(self):
        with self.assertRaises(Exception):
            YouTubeTrendType.objects.create(name='Music', category_id=32768)

    ###########################################
    ### YouTubeTrendType model update tests ###
    ###########################################

    def test_correct_yt_trend_type_model_update(self):

        self.assertEqual(YouTubeTrendType.objects.count(), 1)
        self.assertEqual(self.yt_trend_type.name, 'Music')
        self.assertEqual(self.yt_trend_type.category_id, 10)

        self.yt_trend_type.name = 'Entertainment'
        self.yt_trend_type.category_id = 20
        self.yt_trend_type.save()

        self.assertEqual(YouTubeTrendType.objects.count(), 1)
        self.assertEqual(self.yt_trend_type.name, 'Entertainment')
        self.assertEqual(self.yt_trend_type.category_id, 20)

    # 'name' field

    def test_correct_yt_trend_type_model_update_max_length_name(self):
        self.yt_trend_type.name = 'N' * 100
        self.yt_trend_type.save()
        self.assertEqual(self.yt_trend_type.name, 'N'*100)

    def test_incorrect_yt_trend_type_model_update_without_name(self):
        self.yt_trend_type.name = None
        with self.assertRaises(Exception):
            self.yt_trend_type.full_clean()

    def test_incorrect_yt_trend_type_model_update_blank_name(self):
        self.yt_trend_type.name = ''
        with self.assertRaises(Exception):
            self.yt_trend_type.full_clean()

    def test_incorrect_yt_trend_type_model_update_max_length_name(self):
        self.yt_trend_type.name = 'N' * 101
        with self.assertRaises(Exception):
            self.yt_trend_type.full_clean()

    # 'category_id' field

    def test_correct_yt_trend_type_model_update_max_integer_category_id(self):
        self.yt_trend_type.category_id = 32767
        self.yt_trend_type.save()
        self.assertEqual(self.yt_trend_type.category_id, 32767)

    def test_incorrect_yt_trend_type_model_update_without_category_id(self):
        self.yt_trend_type.category_id = None
        with self.assertRaises(Exception):
            self.yt_trend_type.full_clean()

    def test_incorrect_yt_trend_type_model_update_not_integer_category_id(self):
        self.yt_trend_type.category_id = 'not_integer'
        with self.assertRaises(Exception):
            self.yt_trend_type.full_clean()

    def test_incorrect_yt_trend_type_model_update_max_integer_category_id(self):
        self.yt_trend_type.category_id = 32768
        with self.assertRaises(Exception):
            self.yt_trend_type.full_clean()

    ###########################################
    ### YouTubeTrendType model delete tests ###
    ###########################################

    def test_correct_yt_trend_type_model_delete(self):
        self.assertEqual(YouTubeTrendType.objects.count(), 1)
        self.yt_trend_type.delete()
        self.assertEqual(YouTubeTrendType.objects.count(), 0)
        