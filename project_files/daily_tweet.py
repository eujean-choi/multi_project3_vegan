# !pip install tweepy==4.10.1

import tweepy
import json
from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient("mongodb://readwrite:t01rw@localhost:27017/")
db = client.project


# tweepy.StreamClient 클래스를 상속받는 클래스
class TwitterStream(tweepy.StreamingClient):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        tweet = data['data']
        
        if '@' not in tweet['text'] and tweet['lang'] == 'en':
            db.twitter.insert_one(tweet)
            print(tweet)


def send_data(keyword):
    # 스트림 클라이언트 인스턴스 생성
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPLxggEAAAAAUkllEYIehhsN4%2FgrZFO7xv3SCY8%3D66qsp4JofDNsI5UjdIKJgQTEN62Nsm9I5d6DRRhTaXCtGttGVD'
    client = TwitterStream(BEARER_TOKEN)
    
    # 규칙 삭제
    rules = client.get_rules()
    if rules is None or rules.data is None:
        pass
    else:
        stream_rules = rules.data
        client.delete_rules(ids=list(map(lambda rule: rule.id, stream_rules)))
    
    # 새 규칙 추가
    client.add_rules(tweepy.StreamRule(keyword))
   
    # 스트림 시작
    client.filter(tweet_fields=['author_id', 'lang', 'created_at', 'public_metrics'])
    

if __name__ == '__main__':
    # 1주일 이전에 저장된 링크 삭제
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    db.twitter.delete_many({"created_at": {"$lte": week_ago.isoformat()}})
    
    send_data(keyword="#veganrecipe")
