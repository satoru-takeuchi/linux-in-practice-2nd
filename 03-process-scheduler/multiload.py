#!/bin/bash

MULTICPU=0
PROGNAME=$0
SCRIPT_DIR=$(cd $(dirname $0) && pwd)

usage() {
    exec >&2
    echo "使い方: $PROGNAME [-m] <プロセス数>
    所定の時間動作する負荷処理プロセスを<プロセス数>で指定した数だけ動作させて、すべての終了を待ちます。
    各プロセスにかかった時間を出力します。
    デフォルトではすべてのプロセスは1論理CPU上でだけ動作します。

オプションの意味:
    -m: 各プロセスを複数CPU上で動かせるようにします。"
    exit 1
}

while getopts "m" OPT ; do
    case $OPT in
        m)
            MULTICPU=1
            ;;
        \?)
            usage
            ;;
    esac
done

shift $((OPTIND - 1))

if [ $# -lt 1 ] ; then
    usage
fi

CONCURRENCY=$1

if [ $MULTICPU -eq 0 ] ; then
    # 負荷処理をCPU0でのみ実行できるようにします
    taskset -p -c 0 $$ >/dev/null
fi

for ((i=0;i<CONCURRENCY;i++)) do
    time "${SCRIPT_DIR}/load.py" &
done

for ((i=0;i<CONCURRENCY;i++)) do
    wait
done
