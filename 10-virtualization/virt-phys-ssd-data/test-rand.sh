#!/bin/bash

. config.sh

TOTAL_IO_SIZE=4MiB
BLOCK_SIZE=4k
#EXTRA_OPTION="--thinktime=5"

if [ ! -e ${MOUNT_POINT} ] ; then
  echo "mount point (${MOUNT_POINT}) doesn't exist" >&2
  exit 1
fi

if [ ! -e ${DEVICE_FILE} ] ; then
  echo "device file (${DEVICE_FILE}) doesn't exist" >&2
  exit 1
fi

mount | grep -q ${PART_NAME}
RET=$?
if [ ${RET} != 0 ] ; then
  echo "partition (${PART_FILE}) seems not to be mounted on mount point $(${MOUNT_POINT})" >&2
  exit 1
fi

for READWRITE in randread randwrite; do
  for NUM_JOBS in 1 2 4 8 16 ; do
    echo "readwrite: ${READWRITE}, numjobs: ${NUM_JOBS}" >&2
    echo 3 >/proc/sys/vm/drop_caches
    fio ${EXTRA_OPTION} --direct=1 --name linux-in-diagram --group_reporting --readwrite=${READWRITE} --filename=${DATA_FILE} --filesize=${FILE_SIZE} --size=${TOTAL_IO_SIZE} --bs=${BLOCK_SIZE} --numjobs=${NUM_JOBS} >ssd-${READWRITE}-${NUM_JOBS}.txt
  done
done
