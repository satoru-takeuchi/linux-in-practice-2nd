#!/bin/bash

. ./config

SCHEDULERS="mq-deadline none"

# readahead

OUTFILENAME=${TYPE}-read.txt
rm -f ${OUTFILENAME}

for SCHED in ${SCHEDULERS} ; do
    for READ_AHEAD_KB in 128 0 ; do
        FILENAME=${TYPE}-read-${SCHED}-${READ_AHEAD_KB}.txt
        awk -v sched=${SCHED} -v read_ahead_kb=${READ_AHEAD_KB} '{print sched, read_ahead_kb, $1}' <$FILENAME >>${OUTFILENAME}
    done
done

RAND_NUM_JOBS_LIST=$(seq $(grep -c processor /proc/cpuinfo))

# I/O scheduler

for SCHED in ${SCHEDULERS} ; do
    OUTFILENAME=${TYPE}-randread-${SCHED}.txt
    rm -f ${OUTFILENAME}
    for NUM_JOBS in ${RAND_NUM_JOBS_LIST} ; do
        FILENAME=${TYPE}-randread-${SCHED}-${NUM_JOBS}.txt
        awk -v num_jobs=${NUM_JOBS} '{print num_jobs, $2, $3}' <$FILENAME >>${OUTFILENAME}
    done
done

for SCHED in ${SCHEDULERS} ; do
    OUTFILENAME=${TYPE}-randwrite-${SCHED}.txt
    rm -f ${OUTFILENAME}
    for NUM_JOBS in ${RAND_NUM_JOBS_LIST} ; do
        FILENAME=${TYPE}-randwrite-${SCHED}-${NUM_JOBS}.txt
        awk -v num_jobs=${NUM_JOBS} '{print num_jobs, $2, $3}' <$FILENAME >>${OUTFILENAME}
    done
done
