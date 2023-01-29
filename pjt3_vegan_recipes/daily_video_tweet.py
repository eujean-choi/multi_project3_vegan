from pymongo import MongoClient
from datetime import datetime, timezone
from dateutil import parser
import pytz
import random
import requests

client = MongoClient(host='localhost', port=27017, username='root', password='t01dbpw', authSource='admin')
db = client.project


def today_tw():
    today = datetime.now(timezone.utc)
    t_list = list()
    tweets = db.twitter.find({}, {'_id': 0})

    for tweet in tweets:
        author_id = tweet['author_id']
        tweet_id = tweet['id']
        link = f"https://twitter.com/{author_id}/status/{tweet_id}"

        # 날짜가 오늘인 트윗만 출력
        tweet_date = tweet['created_at']
        tweet_date_parse = parser.parse(tweet_date)

        if (today - tweet_date_parse).seconds / 3600 <= 24:
            t_list.append(link)

    rand_twt = random.choice(t_list)

    embed_query = "https://publish.twitter.com/oembed?url="
    req_json = requests.get(embed_query + rand_twt).json()

    response_text = req_json['html']
    return response_text


def today_yt():
    v_list = list()
    videos = db.youtube.find({}, {'_id': 0})

    kst = pytz.timezone('Asia/Seoul')
    seoul_time = datetime.now(kst)

    for video in videos:
        # 날짜가 오늘인 비디오만 출력
        video_date = video['created_at']
        video_date_parse = parser.parse(video_date)

        if (seoul_time - video_date_parse).seconds / 3600 <= 24:
            v_list.append(video['link'])

    ran_vid = random.choice(v_list)
    return ran_vid
