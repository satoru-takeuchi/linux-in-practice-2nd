#!/usr/bin/python3

import os

ret = os.fork()
if ret == 0:
	os.execve("/bin/echo", ["echo", "fork()とexecve()によって生成されました"], {})
elif ret > 0:
	print("echoコマンドを生成しました")
