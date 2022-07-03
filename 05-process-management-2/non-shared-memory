#!/usr/bin/python3

import os
import sys

data = 1000

print("子プロセス生成前のデータの値: {}".format(data))
pid = os.fork()
if pid < 0:
	print("fork()に失敗しました", file=os.stderr)
elif pid == 0:
	data *= 2
	sys.exit(0)

os.wait()
print("子プロセス終了後のデータの値: {}".format(data))
