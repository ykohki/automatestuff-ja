#! python3
# -*- coding: utf-8 -*-

# 演習プロジェクト 18.13.1 忙しそうに見せる

import pyautogui
import time

print('''10秒ごとにマウスカーソルを左右に少し動かします。
Ctrl-Cで終了します。''')

try:
    dir = -1
    while True:
        time.sleep(10)
        pyautogui.moveRel(dir, 0)
        dir = - dir

except KeyboardInterrupt:
    print('終了')

