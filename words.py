#coding; utf-8

from requests_oauthlib import OAuth1Session
import json
import os
from datetime import datetime
import watt


def puttweet():

    twitter = OAuth1Session(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"],
                            os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])
    msg = watt.getwatt()
    today = datetime.now()
    if msg != "":
        params = {"status": msg}
        # print(params)
        req = twitter.post(
            "https://api.twitter.com/1.1/statuses/update.json", params=params)
        print(today, req.status_code, msg)
    else:
        print(today, '閾値以下なのでTweetしません')


if __name__ == "__main__":
    puttweet()
