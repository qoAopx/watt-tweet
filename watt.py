# -*- coding: utf-8 -*-

import sys
import urllib.request
import json


def getwatt():
    # 情報取得
    feedinput = None
    feed_url = "http://tepco-usage-api.appspot.com/latest.json"
    buf = ""
    try:
        response = urllib.request.urlopen(feed_url)
        #print('url:', response.geturl())
        #print('code:', response.getcode())
        #print('Content-Type:', response.info()['Content-Type'])
        d = json.loads(response.read().decode('utf8'))
        # print(d)
        response.close()

        capacity = None
        saving = None
        usage = None
        hour = None

        if d["hour"] is not None:
            hour = d["hour"]
        if d["capacity"] is not None:
            capacity = d["capacity"]
        if d["saving"] is not None:
            saving = d["saving"]
        if d["usage"] is not None:
            usage = d["usage"]

        per = int(usage) * 1.0 / int(capacity) * 1.0 * 100
        remain = 100.0 - per
        buf = '%s時台 電力使用量(万kW) %d / %d = %.1f%% , 残り %.1f%%' % (hour,
                                                                usage, capacity, per, remain)
        if saving is True:
            buf += ' , 計画停電中です。'
        else:
            buf += ' , 計画停電してません。'

        buf += ' ※2017年4月から残り10%以下の場合のみつぶやくようにしました。'

        print("info", buf)
        if (per > 90.0):
            return buf
        else:
            return ""
            # return buf

    except error:
        print('except', error)
        return ""


if __name__ == "__main__":
    print(getwatt())
