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

class WordGoogleTrendsTest(TestCase):

    def test_correct_country_daily_period(self):

        query = """
            query{
                wordGoogleTrends(word:"Mercadona", country:"Spain", periodType:"daily"){
                    id,
                    trendDatetime,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)

    def test_correct_country_weekly_period(self):

        query = """
            query{
                wordGoogleTrends(word:"Mercadona", country:"Spain", periodType:"weekly"){
                    id,
                    trendDatetime,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)

    def test_correct_country_monthly_period(self):

        query = """
            query{
                wordGoogleTrends(word:"Mercadona", country:"Spain", periodType:"monthly"){
                    id,
                    trendDatetime,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)

    def test_unknow_country(self):

        query = """
            query{
                wordGoogleTrends(word:"Mercadona", country:"Not country", periodType:"daily"){
                    id,
                    trendDatetime,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordGoogleTrends']), 0)

    def test_unknow_period_type(self):
            
            query = """
                query{
                    wordGoogleTrends(word:"Mercadona", country:"Spain", periodType:"Not period type"){
                        id,
                        trendDatetime,
                        value
                    }
                }
            """
    
            schema = graphene.Schema(query=Query)
            result = schema.execute(query)
            self.assertIsNone(result.errors)
            self.assertEqual(len(result.data['wordGoogleTrends']), 0)

class WordRelatedTopicsTest(TestCase):

    def test_correct_country_daily_period(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"daily", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 5)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 5)

    def test_correct_country_weekly_period(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"weekly", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 5)

    def test_correct_country_monthly_period(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"monthly", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 5)

    def test_unknow_country(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Not country", periodType:"daily", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 0)

    def test_unknow_period_type(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"Not period type", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 0)

    def test_unknow_topics_number(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"daily"){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 10)

class YouTubeTrendsTest(TestCase):
    
    def test_correct_country_defined_trends_number_default_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Default", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
    
    def test_correct_country_defined_trends_number_film_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Film & Animation", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
    
    def test_correct_country_defined_trends_number_music_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Music", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
    
    def test_correct_country_defined_trends_number_sports_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Sports", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
    
    def test_correct_country_defined_trends_number_gaming_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Gaming", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_correct_country_defined_trends_number_entertainment_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Entertainment", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_correct_country_defined_trends_number_news_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"News & Politics", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_correct_country_defined_trends_number_science_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Science & Technology", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_correct_country_big_trends_number(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Default", trendsNumber:500){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 25)

    def test_correct_country_undefined_trends_number(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Default"){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_unknown_country(self):

        query = """
            query{
                countryYouTubeTrends(country:"Not coutry", trendType:"Default", trendsNumber:50){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 0)
    
    def test_unknown_trend_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Not trend type", trendsNumber:5){
                    id,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 0)
