import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from datasets import load_dataset
import pickle
from utils.apis.twitter import get_relevant_tweets
from utils.apis.youtube import get_relevant_comments
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

def model_predict(word, video_id):
    
    global tokenizer
    if not tokenizer:
        try:
            with open('tokenizer.pkl', 'rb') as f:
                tokenizer = pickle.load(f)
        except:
            tokenizer = init_tokenizer()

    texts = []
    if word != None and video_id == None:
        texts = get_relevant_tweets(word)
    elif word == None and video_id != None:
        texts = get_relevant_comments(video_id, 50)

    if len(texts) == 0:
        return None, None, None, None

    all_res = []
    
    model = keras.models.load_model('trained_model.h5')

    negative, neutral, positive = 0, 0, 0

    for text in texts:
        seq = get_sequences(tokenizer,[text])
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

def load_trend_emotions(word, video_id):
    
    if word != None and video_id == None:
        emotion, negative, neutral, positive = model_predict(word, None)

        if not emotion or not negative or not neutral or not positive:
            return None

        if TrendEmotion.objects.filter(word=word).exists():
            TrendEmotion.objects.filter(word=word).delete()

        te = TrendEmotion(word=word, majority_emotion=emotion, negative_emotion=negative, neutral_emotion=neutral, positive_emotion=positive)
        te.save()

    elif word == None and video_id != None:
        emotion, negative, neutral, positive = model_predict(None, video_id)

        if not emotion or not negative or not neutral or not positive:
            return None

        if TrendEmotion.objects.filter(video_id=video_id).exists():
            TrendEmotion.objects.filter(video_id=video_id).delete()

        te = TrendEmotion(video_id=video_id, majority_emotion=emotion, negative_emotion=negative, neutral_emotion=neutral, positive_emotion=positive)
        te.save()