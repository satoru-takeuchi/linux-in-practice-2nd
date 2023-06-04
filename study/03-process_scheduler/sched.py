#!/usr/bin/python3

import sys
import time
import os
import plot_sched

# 実験に適した負荷を見つもるための前処理にかける負荷。
# このプログラムの実行に時間がかかりすぎるような場合は値を小さくしてください。
# 反対にすぐ終わってしまうような場合は値を大きくしてください。
NLOOP_FOR_ESTIMATION=100000000
nloop_per_msec = None
progname = sys.argv[0]

def usage():
  print("""使い方: {} <プロセス数>
    * 論理CPU0上で<プロセス数>の数だけ同時に100ミリ秒程度CPUリソースを消費する負荷処理プロセスを起動した後に、すべてのプロセスの終了を待つ。
    * "sched-<プロセス数>.jpg"というファイルに実行結果を示したグラフを書き出す。
    * グラフのx軸は負荷処理プロセス開始からの経過時間[ミリ秒]、y軸は進捗[%]""".format(progname, file=sys.stderr))
  sys.exit(1)

def estimate_loops_per_msec():
  before = time.perf_counter()
  for _ in range(NLOOP_FOR_ESTIMATION):
    pass
  after = time.perf_counter()
  return int(NLOOP_FOR_ESTIMATION/(after-before)/1000)

def child_fn(n, start):
  progress = 100 * [None]
  for i in range(100):
    for j in range(nloop_per_msec):
      pass
    progress[i] = time.perf_counter()
  f = open(f"{n}.data", "w")
  for i in range(100):
    f.write(f"{(progress[i]-start)*1000}\t{i}\n")
  f.close()
  exit(0)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    usage()
  
  concurrency = int(sys.argv[1])

  print(f"sys.argv: {sys.argv}")

  if concurrency < 1:
    print(f"<並列度>は1以上の整数にしてください: {concurrency}")
    usage()
  
  # 論理CPU0上での実行を強制
  os.sched_setaffinity(0, {0})

  nloop_per_msec = estimate_loops_per_msec()

  start = time.perf_counter()

  for i in range(concurrency):
    pid = os.fork()
    print(f"pid: {pid}")
    if (pid < 0):
      exit(1)
    elif pid == 0:
      child_fn(i, start)

  for i in range(concurrency):
    os.wait()
  
  plot_sched.plot_sched(concurrency)
