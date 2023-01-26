from django.test import TestCase
from main.models import Country, YouTubeTrendType, YouTubeTrend, YouTubeCountryTrend
from datetime import datetime
import pytz

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
    
class YouTubeTrendModelTest(TestCase):

    def setUp(self):
        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/br.svg', woeid=455189, pn='brazil')
        yt_trend_type = YouTubeTrendType.objects.create(name='Music', category_id=10)
        self.yt_country_trend = YouTubeCountryTrend.objects.create(country=country, trend_type=yt_trend_type)
        self.yt_trend = YouTubeTrend.objects.create(
            title='title',
            published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
            thumbnail='https://www.youtube.com/',
            view_count=1000,
            like_count=100,
            comment_count=50,
            channel_title='channel_title',
            country_trend=self.yt_country_trend
        )

    #########################################
    ### YouTubeTrend model creation tests ###
    #########################################

    def test_correct_yt_trend_model_create(self):

        self.assertEqual(YouTubeTrend.objects.count(), 1)
        self.assertEqual(self.yt_trend.title, 'title')
        self.assertEqual(self.yt_trend.published_at, datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC))
        self.assertEqual(self.yt_trend.thumbnail, 'https://www.youtube.com/')
        self.assertEqual(self.yt_trend.view_count, 1000)
        self.assertEqual(self.yt_trend.like_count, 100)
        self.assertEqual(self.yt_trend.comment_count, 50)
        self.assertEqual(self.yt_trend.channel_title, 'channel_title')
        self.assertEqual(self.yt_trend.country_trend, self.yt_country_trend)
        self.assertTrue(isinstance(self.yt_trend, YouTubeTrend))
        self.assertEqual(self.yt_trend.__str__(), self.yt_trend.title)

    # 'title' field

    def test_correct_yt_trend_model_create_max_length_title(self):
        yt_trend = YouTubeTrend.objects.create(
            title='T' * 200,
            published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
            thumbnail='https://www.youtube.com/',
            view_count=1000,
            like_count=100,
            comment_count=50,
            channel_title='channel_title',
            country_trend=self.yt_country_trend
        )
        self.assertEqual(yt_trend.title, 'T'*200)

    def test_incorrect_yt_trend_model_create_without_title(self):
        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title=None,
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    def test_incorrect_yt_trend_model_create_blank_title(self):
        with self.assertRaises(Exception):
            yt_trend = YouTubeTrend.objects.create(
                title='',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )
            yt_trend.full_clean()

    def test_incorrect_yt_trend_model_create_max_length_title(self):
        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='T'*201,
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    # 'published_at' field

    def test_incorrect_yt_trend_model_creation_without_published_at(self):
        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=None,
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )
        
    def test_incorrect_yt_trend_model_creation_not_datetime_published_at(self):
        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at='not_datetime',
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    # 'thumbnail' field

    def test_correct_yt_trend_model_creation_max_length_thumbnail(self):
        yt_trend = YouTubeTrend.objects.create(
            title='title',
            published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
            thumbnail='https://www.'+ 't'*83 +'.com/',
            view_count=1000,
            like_count=100,
            comment_count=50,
            channel_title='channel_title',
            country_trend=self.yt_country_trend
        )
        self.assertEqual(yt_trend.thumbnail, 'https://www.'+ 't'*83 +'.com/')

    def test_incorrect_yt_trend_model_creation_without_thumbnail(self):
        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail=None,
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    def test_incorrect_yt_trend_model_creation_blank_thumbnail(self):
        with self.assertRaises(Exception):
            yt_trend = YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )
            yt_trend.full_clean()

    def test_incorrect_yt_trend_model_creation_not_url_thumbnail(self):
        with self.assertRaises(Exception):
            yt_trend = YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='not_url',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )
            yt_trend.full_clean()

    def test_incorrect_yt_trend_model_creation_max_length_thumbnail(self):
        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.'+ 't'*84 +'.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    # 'view_count' field

    def test_correct_yt_trend_model_creation_max_value_view_count(self):

        yt_trend = YouTubeTrend.objects.create(
            title='title',
            published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
            thumbnail='https://www.youtube.com/',
            view_count=9223372036854775807,
            like_count=100,
            comment_count=50,
            channel_title='channel_title',
            country_trend=self.yt_country_trend
        )
        self.assertEqual(yt_trend.view_count, 9223372036854775807)

    def test_incorrect_yt_trend_model_creation_not_integer_view_count(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count='not_integer',
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    def test_incorrect_yt_trend_model_creation_max_value_view_count(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=9223372036854775808,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    # 'like_count' field

    def test_correct_yt_trend_model_creation_max_value_like_count(self):

        yt_trend = YouTubeTrend.objects.create(
            title='title',
            published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
            thumbnail='https://www.youtube.com/',
            view_count=1000,
            like_count=2147483647,
            comment_count=50,
            channel_title='channel_title',
            country_trend=self.yt_country_trend
        )
        self.assertEqual(yt_trend.like_count, 2147483647)

    def test_incorrect_yt_trend_model_creation_not_integer_like_count(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count='not_integer',
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    def test_incorrect_yt_trend_model_creation_max_value_like_count(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=2147483648,
                comment_count=50,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    # 'comment_count' field

    def test_correct_yt_trend_model_creation_max_value_comment_count(self):

        yt_trend = YouTubeTrend.objects.create(
            title='title',
            published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
            thumbnail='https://www.youtube.com/',
            view_count=1000,
            like_count=100,
            comment_count=2147483647,
            channel_title='channel_title',
            country_trend=self.yt_country_trend
        )
        self.assertEqual(yt_trend.comment_count, 2147483647)

    def test_incorrect_yt_trend_model_creation_not_integer_comment_count(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count='not_integer',
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    def test_incorrect_yt_trend_model_creation_max_value_comment_count(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=2147483648,
                channel_title='channel_title',
                country_trend=self.yt_country_trend
            )

    # 'channel_title' field

    def test_correct_yt_trend_model_creation_max_length_channel_title(self):

        yt_trend = YouTubeTrend.objects.create(
            title='title',
            published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
            thumbnail='https://www.youtube.com/',
            view_count=1000,
            like_count=100,
            comment_count=50,
            channel_title='C' * 100,
            country_trend=self.yt_country_trend
        )
        self.assertEqual(yt_trend.channel_title, 'C' * 100)

    def test_incorrect_yt_trend_model_creation_without_channel_title(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title=None,
                country_trend=self.yt_country_trend
            )

    def test_incorrect_yt_trend_model_creation_blank_channel_title(self):

        with self.assertRaises(Exception):
            yt_trend = YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='',
                country_trend=self.yt_country_trend
            )
            yt_trend.full_clean()

    def test_incorrect_yt_trend_model_creation_max_length_channel_title(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='C' * 101,
                country_trend=self.yt_country_trend
            )

    # 'country_trend' field

    def test_incorrect_yt_trend_model_creation_without_country_trend(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend=None
            )

    def test_incorrect_yt_trend_model_creation_not_country_trend(self):

        with self.assertRaises(Exception):
            YouTubeTrend.objects.create(
                title='title',
                published_at=datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC),
                thumbnail='https://www.youtube.com/',
                view_count=1000,
                like_count=100,
                comment_count=50,
                channel_title='channel_title',
                country_trend='not_country_trend'
            )

    #######################################
    ### YouTubeTrend model update tests ###
    #######################################

    def test_correct_yt_trend_model_update(self):

        country = Country.objects.create(name='Argentina', native_name='Argentina', acronym='AR', flag='https://flagcdn.com/ar.svg', woeid=332471, pn='argentina')
        yt_trend_type = YouTubeTrendType.objects.create(name='Sports', category_id=17) 
        yt_country_trend = YouTubeCountryTrend.objects.create(country=country, trend_type=yt_trend_type)

        self.assertEqual(self.yt_trend.title, 'title')
        self.assertEqual(self.yt_trend.published_at, datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC))
        self.assertEqual(self.yt_trend.thumbnail, 'https://www.youtube.com/')
        self.assertEqual(self.yt_trend.view_count, 1000)
        self.assertEqual(self.yt_trend.like_count, 100)
        self.assertEqual(self.yt_trend.comment_count, 50)
        self.assertEqual(self.yt_trend.channel_title, 'channel_title')
        self.assertEqual(self.yt_trend.country_trend, self.yt_country_trend)

        self.yt_trend.title = 'new_title'
        self.yt_trend.published_at = datetime(2019, 1, 2, 0, 0, 0, 0, pytz.UTC)
        self.yt_trend.thumbnail = 'https://www.youtube_update.com/'
        self.yt_trend.view_count = 2000
        self.yt_trend.like_count = 200
        self.yt_trend.comment_count = 100
        self.yt_trend.channel_title = 'new_channel_title'
        self.yt_trend.country_trend = yt_country_trend
        self.yt_trend.save()

        self.assertEqual(self.yt_trend.title, 'new_title')
        self.assertEqual(self.yt_trend.published_at, datetime(2019, 1, 2, 0, 0, 0, 0, pytz.UTC))
        self.assertEqual(self.yt_trend.thumbnail, 'https://www.youtube_update.com/')
        self.assertEqual(self.yt_trend.view_count, 2000)
        self.assertEqual(self.yt_trend.like_count, 200)
        self.assertEqual(self.yt_trend.comment_count, 100)
        self.assertEqual(self.yt_trend.channel_title, 'new_channel_title')
        self.assertEqual(self.yt_trend.country_trend, yt_country_trend)

    # 'title' field

    def test_correct_yt_trend_model_update_max_length_title(self):

        self.assertEqual(self.yt_trend.title, 'title')

        self.yt_trend.title = 'T' * 200
        self.yt_trend.save()

        self.assertEqual(self.yt_trend.title, 'T' * 200)

    def test_incorrect_yt_trend_model_update_without_title(self):

        self.assertEqual(self.yt_trend.title, 'title')

        with self.assertRaises(Exception):
            self.yt_trend.title = None
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_blank_title(self):
            
            self.assertEqual(self.yt_trend.title, 'title')
    
            with self.assertRaises(Exception):
                self.yt_trend.title = ''
                self.yt_trend.save()
                self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_max_length_title(self):
            
            self.assertEqual(self.yt_trend.title, 'title')
    
            with self.assertRaises(Exception):
                self.yt_trend.title = 'T' * 201
                self.yt_trend.save()
                self.yt_trend.full_clean()

    # 'published_at' field

    def test_incorrect_yt_trend_model_update_without_published_at(self):

        self.assertEqual(self.yt_trend.published_at, datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC))

        with self.assertRaises(Exception):
            self.yt_trend.published_at = None
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_not_datetime_published_at(self):

        self.assertEqual(self.yt_trend.published_at, datetime(2019, 1, 1, 0, 0, 0, 0, pytz.UTC))

        with self.assertRaises(Exception):
            self.yt_trend.published_at = 'not_datetime'
            self.yt_trend.save()
            self.yt_trend.full_clean()

    # 'thumbnail' field

    def test_correct_yt_trend_model_update_max_length_thumbnail(self):

        self.assertEqual(self.yt_trend.thumbnail, 'https://www.youtube.com/')

        self.yt_trend.thumbnail = 'https://www.'+ 't'*83 +'.com/'
        self.yt_trend.save()

        self.assertEqual(self.yt_trend.thumbnail, 'https://www.'+ 't'*83 +'.com/')

    def test_incorrect_yt_trend_model_update_without_thumbnail(self):

        self.assertEqual(self.yt_trend.thumbnail, 'https://www.youtube.com/')

        with self.assertRaises(Exception):
            self.yt_trend.thumbnail = None
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_blank_thumbnail(self):

        self.assertEqual(self.yt_trend.thumbnail, 'https://www.youtube.com/')

        with self.assertRaises(Exception):
            self.yt_trend.thumbnail = ''
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_not_url_thumbnail(self):

        self.assertEqual(self.yt_trend.thumbnail, 'https://www.youtube.com/')

        with self.assertRaises(Exception):
            self.yt_trend.thumbnail = 'not_url'
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_max_length_thumbnail(self):

        self.assertEqual(self.yt_trend.thumbnail, 'https://www.youtube.com/')

        with self.assertRaises(Exception):
            self.yt_trend.thumbnail = 'https://www.'+ 't'*84 +'.com/'
            self.yt_trend.save()
            self.yt_trend.full_clean()

    # 'view_count' field

    def test_correct_yt_trend_model_update_max_value_view_count(self):

        self.assertEqual(self.yt_trend.view_count, 1000)

        self.yt_trend.view_count = 9223372036854775807
        self.yt_trend.save()

        self.assertEqual(self.yt_trend.view_count, 9223372036854775807)

    def test_incorrect_yt_trend_model_update_not_integer_view_count(self):

        self.assertEqual(self.yt_trend.view_count, 1000)

        with self.assertRaises(Exception):
            self.yt_trend.view_count = 'not_integer'
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_max_value_view_count(self):

        self.assertEqual(self.yt_trend.view_count, 1000)

        with self.assertRaises(Exception):
            self.yt_trend.view_count = 9223372036854775808
            self.yt_trend.save()
            self.yt_trend.full_clean()

    # 'like_count' field

    def test_correct_yt_trend_model_update_max_value_like_count(self):

        self.assertEqual(self.yt_trend.like_count, 100)

        self.yt_trend.like_count = 2147483647
        self.yt_trend.save()

        self.assertEqual(self.yt_trend.like_count, 2147483647)

    def test_incorrect_yt_trend_model_update_not_integer_like_count(self):

        self.assertEqual(self.yt_trend.like_count, 100)

        with self.assertRaises(Exception):
            self.yt_trend.like_count = 'not_integer'
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_max_value_like_count(self):

        self.assertEqual(self.yt_trend.like_count, 100)

        with self.assertRaises(Exception):
            self.yt_trend.like_count = 2147483648
            self.yt_trend.save()
            self.yt_trend.full_clean()

    # 'comment_count' field

    def test_correct_yt_trend_model_update_max_value_comment_count(self):

        self.assertEqual(self.yt_trend.comment_count, 50)

        self.yt_trend.comment_count = 2147483647
        self.yt_trend.save()

        self.assertEqual(self.yt_trend.comment_count, 2147483647)

    def test_incorrect_yt_trend_model_update_not_integer_comment_count(self):

        self.assertEqual(self.yt_trend.comment_count, 50)

        with self.assertRaises(Exception):
            self.yt_trend.comment_count = 'not_integer'
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_max_value_comment_count(self):

        self.assertEqual(self.yt_trend.comment_count, 50)

        with self.assertRaises(Exception):
            self.yt_trend.comment_count = 2147483648
            self.yt_trend.save()
            self.yt_trend.full_clean()

    # 'channel_title' field

    def test_correct_yt_trend_model_update_max_length_channel_title(self):

        self.assertEqual(self.yt_trend.channel_title, 'channel_title')

        self.yt_trend.channel_title = 'C'*100
        self.yt_trend.save()

        self.assertEqual(self.yt_trend.channel_title, 'C'*100)

    def test_incorrect_yt_trend_model_update_without_channel_title(self):

        self.assertEqual(self.yt_trend.channel_title, 'channel_title')

        with self.assertRaises(Exception):
            self.yt_trend.channel_title = None
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_blank_channel_title(self):

        self.assertEqual(self.yt_trend.channel_title, 'channel_title')

        with self.assertRaises(Exception):
            self.yt_trend.channel_title = ''
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_max_length_channel_title(self):

        self.assertEqual(self.yt_trend.channel_title, 'channel_title')

        with self.assertRaises(Exception):
            self.yt_trend.channel_title = 'C'*101
            self.yt_trend.save()
            self.yt_trend.full_clean()

    # 'country_trend' field

    def test_incorrect_yt_trend_model_update_without_country_trend(self):

        self.assertEqual(self.yt_trend.country_trend, self.yt_country_trend)

        with self.assertRaises(Exception):
            self.yt_trend.country_trend = None
            self.yt_trend.save()
            self.yt_trend.full_clean()

    def test_incorrect_yt_trend_model_update_not_country_trend(self):

        self.assertEqual(self.yt_trend.country_trend, self.yt_country_trend)

        with self.assertRaises(Exception):
            self.yt_trend.country_trend = 'not_country'
            self.yt_trend.save()
            self.yt_trend.full_clean()

    #######################################
    ### YouTubeTrend Model delete tests ###
    #######################################

    def test_correct_yt_trend_model_delete(self):

        self.assertEqual(YouTubeTrend.objects.count(), 1)

        self.yt_trend.delete()

        self.assertEqual(YouTubeTrend.objects.count(), 0)