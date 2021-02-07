# 電力使用量Tweet

- 毎時電力使用量を投稿します。電力使用量が90％を超えた場合のみTweetします。
- もともとGCP AppEngineで動かしてたものを移植しました。

## 設定方法

```sh
heroku config:set --app "[APPNAME]" CONSUMER_KEY="XXX"
heroku config:set --app "[APPNAME]" CONSUMER_SECRET="XXX"
heroku config:set --app "[APPNAME]" ACCESS_TOKEN_KEY="XXX"
heroku config:set --app "[APPNAME]" ACCESS_TOKEN_SECRET="XXX"
```

## 参考

<https://qiita.com/RollSystems/items/408cb4267a9a9770dfc9>
