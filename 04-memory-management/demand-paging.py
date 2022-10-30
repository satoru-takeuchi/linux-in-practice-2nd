#!/usr/bin/python3

import mmap
import time
import datetime

ALLOC_SIZE  = 100 * 1024 * 1024
ACCESS_UNIT = 10 * 1024 * 1024
PAGE_SIZE   = 4096

def show_message(msg):
	print("{}: {}".format(datetime.datetime.now().strftime("%H:%M:%S"), msg))

show_message("新規メモリ領域獲得前。Enterキーを押すと100MiBの新規メモリ領域を獲得します: ")
input()

# mmap()システムコールの呼び出しによって100MiBのメモリ領域を獲得
memregion = mmap.mmap(-1, ALLOC_SIZE, flags=mmap.MAP_PRIVATE)
show_message("新規メモリ領域を獲得しました。Enterキーを押すと1秒に10MiBづつ、合計100MiBの新規メモリ領域にアクセスします: ")
input()

for i in range(0, ALLOC_SIZE, PAGE_SIZE):
	memregion[i] = 0
	if i%ACCESS_UNIT == 0 and i != 0:
		show_message("{} MiBアクセスしました".format(i//(1024*1024)))
		time.sleep(1)

show_message("新規獲得したメモリ領域のすべてのアクセスしました。Enterキーを押すと終了します: ")
input()
