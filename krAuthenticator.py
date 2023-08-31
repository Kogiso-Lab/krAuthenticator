import json
import requests
from tkinter import messagebox
import os
import sys
from datetime import datetime
import json
import socket
import tkinter as tk

# 主ウィンドウが表示されないようにする
root = tk.Tk()
root.withdraw()  

def is_connected():
    try:
        # Googleの公共DNSサーバーに接続を試みる
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def can_access_web():
    try:
        response = requests.get('https://www.google.com')
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False


# 実行ファイルの位置を取得（PyInstaller対応）
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

# data.jsonの絶対パスを作成
json_path = os.path.join(current_dir, 'login_info.json')

# 認証用のエンドポイントURLを指定してください
auth_url = "https://webauth.omu.ac.jp/portal/logon.cgi"

def authenticate(username, password):
    payload = {"PtUser": username, "PtPwd": password, "PtButton": "Logon"}
    response = requests.post(auth_url, data=payload, verify=False)
    
    if "ログインに失敗しました" in response.text:
        messagebox.showerror("krAuthenticator", "認証失敗")
        pass
    else:
        messagebox.showinfo("krAuthenticator", "認証成功")

# jsonファイルからデータを読み込む
try:
    file = json.load(open(json_path, "r"))
    # ユーザー名とパスワードを取得します
    username = file["username"]
    password = file["password"]
    
    # 日付を取得してPythonのdatetimeオブジェクトに変換
    stored_date_str = file["date"]
    stored_date = datetime.strptime(stored_date_str, '%Y-%m-%d').date()
    
    # 現在の日付を取得
    current_date = datetime.now().date()

    # 現在の日付と保存された日付を比較
    is_past_date = stored_date < current_date

    # 時間を超えていた時，jsonファイルをさ削除する
    if is_past_date:
        os.remove(json_path)
    
    if not is_connected() or not can_access_web():
        # 認証を試みます
        authenticate(
                username, 
                password
            )
    else:
        messagebox.showinfo("krAuthenticator", "ネットワークに接続されています．")
        
except FileNotFoundError:
    messagebox.showerror(
            "krAuthenticator", 
            "パスワード情報が見つかりませんでした．"
            +"exeファイルと同じディレクトリにlogin_info.jsonを配置してください．"
            +str(sys.exc_info()[0])
            )
except :
    messagebox.showerror(
            "krAuthenticator", 
            "エラーが発生しました．"
            +str(sys.exc_info()[0]))