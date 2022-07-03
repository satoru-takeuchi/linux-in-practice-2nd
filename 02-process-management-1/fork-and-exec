#!/usr/bin/python3

import os, sys

ret = os.fork()
if ret == 0:
	print("子プロセス: pid={}, 親プロセスのpid={}".format(os.getpid(), os.getppid()))
	os.execve("/bin/echo", ["echo", "pid={} からこんにちは".format(os.getpid())], {})
	exit()
elif ret > 0:
	print("親プロセス: pid={}, 子プロセスのpid={}".format(os.getpid(), ret))
	exit()

sys.exit(1)
