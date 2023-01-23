import requests
from decouple import config
from datetime import datetime

from main.models import Country, YouTubeTrend, YouTubeTrendType, YouTubeCountryTrend

def get_country_trends(country_name, trend_type):

    youtube_api_key = config('YOUTUBE_API_KEY')

    try:
        country = Country.objects.get(name=country_name)
        acronym = country.acronym

        if YouTubeTrendType.objects.filter(name=trend_type).exists():
            if trend_type != 'Default':
                category_id = YouTubeTrendType.objects.get(name=trend_type).category_id
                url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=" + acronym + "&videoCategoryId=" + str(category_id) + "&key=" + youtube_api_key
            else:
                url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=" + acronym + "&key=" + youtube_api_key

            response = requests.get(url)
            return get_country_trends_aux(response, url, [], 0)
        return []
    except:
        return []

def get_country_trends_aux(response, url, res, trends_number):

    res_aux = res.copy()

    if response.status_code == 200 and trends_number <= 20:
        data = response.json()
        videos = data['items']

        for video in videos:
            title = video['snippet']['title']
            published_at = video['snippet']['publishedAt']
            thumbnail = get_thumbnail_url(video)
            channel_title = video['snippet']['channelTitle']
            views, likes, comments = get_video_staistics(video['id'])
            aux = [title, published_at, thumbnail, channel_title, views, likes, comments]
            res_aux.append(aux)

        if 'nextPageToken' in data.keys():
            page_token = data['nextPageToken']
            url = url.split("&pageToken=")[0] + "&pageToken=" + page_token
            response = requests.get(url)
            
            return get_country_trends_aux(response, url, res_aux, trends_number + 5)
        else:
            return res
    else:
        return res

def get_thumbnail_url(video):

    thumbnails = video['snippet']['thumbnails']
    thumbnails_keys = video['snippet']['thumbnails'].keys()

    if 'maxres' in thumbnails_keys:
        return thumbnails['maxres']['url']
    if 'standard' in thumbnails_keys:
        return thumbnails['standard']['url']
    elif 'high' in thumbnails_keys:
        return thumbnails['high']['url']
    elif 'medium' in thumbnails_keys:
        return thumbnails['medium']['url']
    elif 'default' in thumbnails_keys:
        return thumbnails['default']['url']
    else:
        return ""

def get_video_staistics(video_id):

    youtube_api_key = config('YOUTUBE_API_KEY')

    url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + video_id + "&key=" + youtube_api_key
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        views = data['items'][0]['statistics']['viewCount']
        likes = data['items'][0]['statistics']['likeCount']
        comments = data['items'][0]['statistics']['commentCount']
        try:
            return int(views), int(likes), int(comments)
        except:
            return None, None, None
    else:
        return None, None, None

def load_trending_types():
    
    if YouTubeTrendType.objects.count() == 0:

        trending_types = {
            "Default": 0,
            "Film & Animation": 1,
            "Music": 10,
            "Sports": 17,
            "Gaming": 20,
            "Entertainment": 24,
            "News & Politics": 25,
            "Science & Technology": 28
        }

        for t in trending_types:
            yt = YouTubeTrendType(name=t, category_id=trending_types[t])
            yt.save()

def load_country_trends(country_name, trend_type):

    load_trending_types()
    trends = get_country_trends(country_name, trend_type)

    if len(trends) > 0:

        country = Country.objects.get(name=country_name)

        if YouTubeTrendType.objects.filter(name=trend_type).exists():
            yt = YouTubeTrendType.objects.get(name=trend_type)

            if YouTubeCountryTrend.objects.filter(country=country, trend_type=yt).exists():
                YouTubeCountryTrend.objects.filter(country=country, trend_type=yt).delete()

            yct = YouTubeCountryTrend(country=country, trend_type=yt)
            yct.save()

            for t in trends:
                yt = YouTubeTrend(title=t[0].encode("utf-8"), published_at=datetime.strptime(t[1], "%Y-%m-%dT%H:%M:%SZ"), thumbnail=t[2], channel_title=t[3], view_count=t[4], like_count=t[5], comment_count=t[6], country_trend=yct)
                yt.save()