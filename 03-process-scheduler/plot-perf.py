#!/usr/bin/python3

import sys
import plot_sched

def usage():
    print("""使い方: {} <最大プロセス数>
    * cpuperfプログラムの実行結果を保存した"perf.data"ファイルをもとに性能情報を示すグラフを作る。
    * "avg-tat.jpg"ファイルに平均ターンアラウンドタイムのグラフを保存する。
    * "throughput.jpg"ファイルにスループットのグラフを保存する。""".format(progname, file=sys.stderr))
    sys.exit(1)

progname = sys.argv[0]

if len(sys.argv) < 2:
    usage()

max_nproc = int(sys.argv[1])
plot_sched.plot_avg_tat(max_nproc)
plot_sched.plot_throughput(max_nproc)
