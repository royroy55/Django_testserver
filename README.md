# Django_testserver

自分のアプリのテスト用にDjangoで作ったサーバです。  
urlさえ書き換えれば適当なアプリからのPOSTのテストには使えると思いたい。

## 簡単な機能の説明
post_testってurlを叩けば飛んできたJSONを適当にperseしてデータベースに保存してくれます。  
testserver/cms/models.pyとtestserver/cms/views.pyを書き換えたらいろんなPOSTのテストに使えると思います。
