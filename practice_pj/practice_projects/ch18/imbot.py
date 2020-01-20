#! python3
# -*- coding: utf-8 -*-

# 演習プロジェクト 18.13.2  Googleハングアウトの自動操作
#
#  Google Talkがサービス終了のため、代わりにGoogleハングアウトを使って
#  複数ユーザにメッセージを送信するプログラム。
#
#  あらかじめ、Googleハングアウトの画面から、送信する相手のアイコンや名前の
#  部分を切り取って、user1.png、user2.png、... という名前のPNGファイルとして
#  保存してください。
#  切り取る箇所は、guide.pngの赤い枠の部分を参照してください。
#  このとき、ユーザを選択せず、背景を白いままにしてください。
#  選択して背景がグレーになった画像だと、うまくマッチできません。
#
#  Googleハングアウトのウィンドウを表示した状態で、
#  次のように本プログラムを実行すると、画像にマッチするユーザに
#  順番にメッセージを送信することができます。
#     python imbot.py メッセージ
#  動作中は、マウスを触らないようにしてください。
#

import pyautogui
import pyperclip
import sys
import os
import re

# pyautogui.typewrite()では日本語を入力できないので、
# クリップボード経由でペーストする
def mytypewrite(s):
    saved_clipboard = pyperclip.paste()
    pyperclip.copy(s)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy(saved_clipboard)

# 画像を見つけて、クリックする。見つからなければFalseを返す。
def click_image(image):
    position = pyautogui.locateOnScreen(image)
    if not position:
        return False
    position = pyautogui.center(position)
    pyautogui.click(position)
    return True

# ユーザをクリックして、メッセージを送信する。
def send_message(username, message):
    for i in range(2):
        if click_image(username):
            # 画像が見つかれば、メッセージを送信する。
            print('{}に送信中。'.format(username))
            mytypewrite(message)
            pyautogui.typewrite('\n')
            return
        elif click_image('newconv.png'):
            # 画像がマッチしなければ、ユーザが選択中で背景がグレーに
            # なっていることが考えられるので、いったん、 
            #「新しい会話」をクリックして、選択を解除して背景を白くする。
            # そして、もう1回だけリトライする
            continue
        else:
            # 「新しい会話」(newconv.png)が見つからない場合は、
            # みなさんの環境で新しい会話の部分を切り取ってnewconv.pngとして
            # 保存しなおしてください。
            print('「新しい会話」が見つかりません。中止します。')
            return

    print('{}に送れませんでした。'.format(username))

if len(sys.argv) < 2:
    sys.exit('使い方: python imbot.py メッセージ')

message = ' '.join(sys.argv[1:])

for filename in os.listdir('./'):
    if re.match(r'user.*\.png', filename, re.I):
        send_message(filename, message)

