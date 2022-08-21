#!/bin/bash

usage() {
    exec >&2
    echo "使い方: $0 [-m] <最大プロセス数>
    1. 'cpuperf.data'というファイルに性能情報を保存する
        * エントリ数は<最大プロセス数>
        * 各行のフォーマットは'<プロセス数> <平均ターンアラウンドタイム[秒]> <スループット[プロセス/秒]>'
    2. 性能情報をもとに平均スループットのグラフを作って'avg-tat.jpg'に保存
    3. 同、スループットのグラフを作って'throughput.jpg'に保存
    
    -mオプションはmultiload.shプログラムにそのまま渡す"
    exit 1
}

measure() {
    local nproc=$1
    local opt=$2
    bash -c "time ./multiload.sh $opt $nproc" 2>&1 | grep real | sed -n -e 's/^.*0m\([.0-9]*\)s$/\1/p' | awk -v nproc=$nproc '
BEGIN{
    sum_tat=0
}
(NR<=nproc){
    sum_tat+=$1
}
(NR==nproc+1) {
    total_real=$1
}
END{
    printf("%d\t%.3f\t%.3f\n", nproc, sum_tat/nproc, nproc/total_real)    
}'
}

while getopts "m" OPT ; do
    case $OPT in
        m)
            MEASURE_OPT="-m"
            ;;
        \?)
            usage
            ;;
    esac
done

shift $((OPTIND - 1))

if [ $# -lt 1 ]; then
    usage
fi

rm -f cpuperf.data
MAX_NPROC=$1
for ((i=1;i<=MAX_NPROC;i++)) ; do
    measure $i $MEASURE_OPT  >>cpuperf.data
done

./plot-perf.py $MAX_NPROC
