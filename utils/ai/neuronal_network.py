import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from datasets import load_dataset
import pickle
from utils.apis.twitter import get_relevant_tweets
from main.models import TrendEmotion

tokenizer = None
index_to_label = {0:'negative', 1:'neutral', 2:'positive'}

def init_tokenizer():
    global tokenizer
    if tokenizer:
        return tokenizer

    dataset = load_dataset("mteb/tweet_sentiment_extraction")
    train = dataset['train']
    texts = [x['text'] for x in train]

    tokenizer = Tokenizer(num_words=1000, oov_token='<UNK>')
    tokenizer.fit_on_texts(texts)

    with open('tokenizer.pkl', 'wb') as f:
        pickle.dump(tokenizer, f)

    return tokenizer

def get_sequences(tokenizer, texts):
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, truncating='post', padding='post', maxlen=35)
    return padded

def model_predict(trend):
    
    global tokenizer
    if not tokenizer:
        try:
            with open('tokenizer.pkl', 'rb') as f:
                tokenizer = pickle.load(f)
        except:
            tokenizer = init_tokenizer()

    tweets = get_relevant_tweets(trend)

    if len(tweets) == 0:
        return None, None, None, None

    all_res = []
    
    model = keras.models.load_model('trained_model.h5')

    negative, neutral, positive = 0, 0, 0

    for tweet in tweets:
        seq = get_sequences(tokenizer,[tweet])
        result = model.predict(np.expand_dims(seq[0], axis=0))[0]

        negative += result[0]
        neutral += result[1]
        positive += result[2]

        all_res.append(np.argmax(result).astype('uint8'))
        
    sum_ = negative + neutral + positive
    total_negative = negative/sum_
    total_neutral = neutral/sum_
    total_positive = positive/sum_
        
    return index_to_label[np.argmax(np.bincount(all_res))], total_negative, total_neutral, total_positive

def load_trend_emotions(trend):
    
    emotion, negative, neutral, positive = model_predict(trend)

    if not emotion or not negative or not neutral or not positive:
        return None

    if TrendEmotion.objects.filter(word=trend).exists():
        TrendEmotion.objects.filter(word=trend).delete()

    te = TrendEmotion(word=trend, majority_emotion=emotion, negative_emotion=negative, neutral_emotion=neutral, positive_emotion=positive)
    te.save()