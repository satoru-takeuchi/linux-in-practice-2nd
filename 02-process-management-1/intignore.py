#!/usr/bin/python3

import signal

# SIGINTシグナルを無視するように設定。第1引数にはハンドラを設定するシグナル(ここではsignal.SIGINT)を、
# 第2引数にはシグナルハンドラ(ここではsignal.SIG_IGN)を指定する。
signal.signal(signal.SIGINT, signal.SIG_IGN)

while True:
	pass
