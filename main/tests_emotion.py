from django.test import TestCase
from main.models import TrendEmotion

# Tests of the TrendEmotion model

class TrendEmotionModelTestCase(TestCase):

    def setUp(self):
        
        self.trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                        neutral_emotion = 0.4, 
                                                        positive_emotion = 0.1,
                                                        sadness_emotion = 0.2,
                                                        fear_emotion = 0.3,
                                                        love_emotion = 0.2,
                                                        surprise_emotion = 0.1,
                                                        anger_emotion = 0.1,
                                                        joy_emotion = 0.1, 
                                                        word = 'test')


    #########################################
    ### TrendEmotion model creation tests ###
    #########################################


    def test_correct_trend_emotion_model_creation(self):

        self.assertEqual(TrendEmotion.objects.count(), 1)
        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)
        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)
        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.assertEqual(self.trend_emotion.word, 'test')
        self.assertTrue(isinstance(self.trend_emotion, TrendEmotion))
        self.assertEqual(self.trend_emotion.__str__(), self.trend_emotion.word + '-' + str(self.trend_emotion.insertion_datetime))


    # 'negative_emotion' field

    def test_correct_trend_emotion_creation_min_value_negative_emotion(self):
            
        trend_emotion = TrendEmotion.objects.create(negative_emotion = 0, 
                                                    neutral_emotion = 0.4, 
                                                    positive_emotion = 0.6,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
        self.assertEqual(trend_emotion.negative_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_negative_emotion(self):
        
        trend_emotion = TrendEmotion.objects.create(negative_emotion = 1, 
                                                    neutral_emotion = 0, 
                                                    positive_emotion = 0,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
        self.assertEqual(trend_emotion.negative_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = -1, 
                                                    neutral_emotion = 0.4, 
                                                    positive_emotion = 0.6,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 1.1, 
                                                    neutral_emotion = 0.4, 
                                                    positive_emotion = 0.6,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = None, 
                                                    neutral_emotion = 0.4, 
                                                    positive_emotion = 0.6,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 'test', 
                                                        neutral_emotion = 0.4, 
                                                        positive_emotion = 0.6,
                                                        sadness_emotion = 0.2,
                                                        fear_emotion = 0.3,
                                                        love_emotion = 0.2,
                                                        surprise_emotion = 0.1,
                                                        anger_emotion = 0.1,
                                                        joy_emotion = 0.1, 
                                                        word = 'test')
            trend_emotion.full_clean()

    # 'neutral_emotion' field

    def test_correct_trend_emotion_creation_min_value_neutral_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                    neutral_emotion = 0, 
                                                    positive_emotion = 0.5,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
        self.assertEqual(trend_emotion.neutral_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_neutral_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion = 0, 
                                                    neutral_emotion = 1, 
                                                    positive_emotion = 0,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
        self.assertEqual(trend_emotion.neutral_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_neutral_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                    neutral_emotion = -1, 
                                                    positive_emotion = 0.5,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_neutral_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                    neutral_emotion = 1.1, 
                                                    positive_emotion = 0.5,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_neutral_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                    neutral_emotion = None, 
                                                    positive_emotion = 0.5,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_neutral_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                    neutral_emotion = 'test', 
                                                    positive_emotion = 0.5,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
            trend_emotion.full_clean()

    # 'positive_emotion' field

    def test_correct_trend_emotion_creation_min_value_positive_emotion(self):
        trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                    neutral_emotion = 0.5, 
                                                    positive_emotion = 0,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
        self.assertEqual(trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_positive_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion = 0, 
                                                    neutral_emotion = 0, 
                                                    positive_emotion = 1,
                                                    sadness_emotion = 0.2,
                                                    fear_emotion = 0.3,
                                                    love_emotion = 0.2,
                                                    surprise_emotion = 0.1,
                                                    anger_emotion = 0.1,
                                                    joy_emotion = 0.1, 
                                                    word = 'test')
        self.assertEqual(trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                        neutral_emotion = 0.5, 
                                                        positive_emotion = -1,
                                                        sadness_emotion = 0.2,
                                                        fear_emotion = 0.3,
                                                        love_emotion = 0.2,
                                                        surprise_emotion = 0.1,
                                                        anger_emotion = 0.1,
                                                        joy_emotion = 0.1, 
                                                        word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                        neutral_emotion = 0.5, 
                                                        positive_emotion = 1.1,
                                                        sadness_emotion = 0.2,
                                                        fear_emotion = 0.3,
                                                        love_emotion = 0.2,
                                                        surprise_emotion = 0.1,
                                                        anger_emotion = 0.1,
                                                        joy_emotion = 0.1, 
                                                        word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                        neutral_emotion = 0.5, 
                                                        positive_emotion = None,
                                                        sadness_emotion = 0.2,
                                                        fear_emotion = 0.3,
                                                        love_emotion = 0.2,
                                                        surprise_emotion = 0.1,
                                                        anger_emotion = 0.1,
                                                        joy_emotion = 0.1, 
                                                        word = 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                        neutral_emotion = 0.5, 
                                                        positive_emotion = 'test',
                                                        sadness_emotion = 0.2,
                                                        fear_emotion = 0.3,
                                                        love_emotion = 0.2,
                                                        surprise_emotion = 0.1,
                                                        anger_emotion = 0.1,
                                                        joy_emotion = 0.1, 
                                                        word = 'test')
            trend_emotion.full_clean()

    # 'word' field

    def test_correct_trend_emotion_creation_max_length_word(self):

        trend_emotion = trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                                    neutral_emotion = 0.5, 
                                                                    positive_emotion = 0,
                                                                    sadness_emotion = 0.2,
                                                                    fear_emotion = 0.3,
                                                                    love_emotion = 0.2,
                                                                    surprise_emotion = 0.1,
                                                                    anger_emotion = 0.1,
                                                                    joy_emotion = 0.1, 
                                                                    word = 't'*100)
        self.assertEqual(trend_emotion.word, 't' * 100)

    def test_incorrect_trend_emotion_creation_blank_word(self):

        with self.assertRaises(Exception):
            trend_emotion = trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                                        neutral_emotion = 0.5, 
                                                                        positive_emotion = 0,
                                                                        sadness_emotion = 0.2,
                                                                        fear_emotion = 0.3,
                                                                        love_emotion = 0.2,
                                                                        surprise_emotion = 0.1,
                                                                        anger_emotion = 0.1,
                                                                        joy_emotion = 0.1, 
                                                                        word = '')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_max_length_word(self):
            
            with self.assertRaises(Exception):
                trend_emotion = trend_emotion = TrendEmotion.objects.create(negative_emotion = 0.5, 
                                                                        neutral_emotion = 0.5, 
                                                                        positive_emotion = 0,
                                                                        sadness_emotion = 0.2,
                                                                        fear_emotion = 0.3,
                                                                        love_emotion = 0.2,
                                                                        surprise_emotion = 0.1,
                                                                        anger_emotion = 0.1,
                                                                        joy_emotion = 0.1, 
                                                                        word = 't'*101)

    #######################################
    ### TrendEmotion model update tests ###
    #######################################

    def test_correct_trend_emotion_update(self):

        self.assertEqual(TrendEmotion.objects.count(), 1)
        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)
        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)
        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.assertEqual(self.trend_emotion.word, 'test')
        self.assertTrue(isinstance(self.trend_emotion, TrendEmotion))
        self.assertEqual(self.trend_emotion.__str__(), self.trend_emotion.word + '-' + str(self.trend_emotion.insertion_datetime))

        self.trend_emotion.negative_emotion = 0.3
        self.trend_emotion.neutral_emotion = 0.6
        self.trend_emotion.positive_emotion = 0.1
        self.trend_emotion.word = 'test2'
        self.trend_emotion.save()

        self.assertEqual(self.trend_emotion.negative_emotion, 0.3)
        self.assertEqual(self.trend_emotion.neutral_emotion, 0.6)
        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.assertEqual(self.trend_emotion.word, 'test2')
        self.assertTrue(isinstance(self.trend_emotion, TrendEmotion))
        self.assertEqual(self.trend_emotion.__str__(), 'test2' + '-' + str(self.trend_emotion.insertion_datetime))


    # 'negative_emotion' field

    def test_correct_trend_emotion_update_min_value_negative_emotion(self):
        
        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)
        self.trend_emotion.negative_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.negative_emotion, 0)

    def test_correct_trend_emotion_update_max_value_negative_emotion(self):
        
        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)
        self.trend_emotion.negative_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.negative_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.negative_emotion = -0.1
            self.trend_emotion.full_clean()
        
    def test_incorrect_trend_emotion_update_greater_than_one_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.negative_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.negative_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.negative_emotion = 'test'
            self.trend_emotion.save()

    # 'neutral_emotion' field

    def test_correct_trend_emotion_update_min_value_neutral_emotion(self):
            
        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)
        self.trend_emotion.neutral_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.neutral_emotion, 0)

    def test_correct_trend_emotion_update_max_value_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)
        self.trend_emotion.neutral_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.neutral_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)

        with self.assertRaises(Exception):
            self.trend_emotion.neutral_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)

        with self.assertRaises(Exception):
            self.trend_emotion.neutral_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)

        with self.assertRaises(Exception):
            self.trend_emotion.neutral_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)

        with self.assertRaises(Exception):
            self.trend_emotion.neutral_emotion = 'test'
            self.trend_emotion.save()

    # 'positive_emotion' field

    def test_correct_trend_emotion_update_min_value_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
            self.trend_emotion.save()

    # 'word' field

    def test_correct_trend_emotion_update_max_length_word(self):
            
        self.assertEqual(self.trend_emotion.word, 'test')
        self.trend_emotion.word = 't' * 100
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.word, 't' * 100)

    def test_incorrect_trend_emotion_update_blank_word(self):

        self.assertEqual(self.trend_emotion.word, 'test')

        with self.assertRaises(Exception):
            self.trend_emotion.word = ''
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_max_length_word(self):

        self.assertEqual(self.trend_emotion.word, 'test')

        with self.assertRaises(Exception):
            self.trend_emotion.word = 't' * 101
            self.trend_emotion.save()

    #######################################
    ### TrendEmotion model delete tests ###
    #######################################


    def test_correct_trend_emotion_model_delete(self):
                
        self.assertEqual(TrendEmotion.objects.count(), 1)
        self.trend_emotion.delete()
        self.assertEqual(TrendEmotion.objects.count(), 0)