# krAuthenticator
- login_info.jsonをexeと同じ位置に配置する
- タスクスケジューラーでネットワークが切れたら実行するようにする．
    - 何時にネットワークが切断されるかなどは決まってないみたいなので下のやつ参照
    - https://victoriavette.com/ja/1734-windows-task-scheduler-trigger-an-event-when-internet-connects-disconnects.html 
- テキトーに作ったのでご愛嬌
- 接続には大学システムのせいで時間かかるので注意

login_info.jsonの内容
```
{
    "password": "パスワード", 
    "username": "sk7777f", 
    "date": "2024-03-31"   # この日付を超えた時に，おいていたファイルを削除する
}
```
