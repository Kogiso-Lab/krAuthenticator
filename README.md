# krAuthenticator
- login_info.jsonをexeと同じ位置に配置する
- exeを毎晩実行するようにする．(0:00だと大学側のシステムが怪しいから00:05とかが良いかな)
- テキトーに作ったのでご愛嬌

login_info.jsonの内容
```
{
    "password": "", パスワード
    "username": "", ユーザ名
    "date": "2024-03-31"   # この日付を超えた時に，おいていたファイルを削除する
}

```
