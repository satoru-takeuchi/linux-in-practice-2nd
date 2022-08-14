#!/bin/bash

while : ; do
  if [ ! -e lock ] ; then
    break
  fi
done
touch lock
TMP=$(cat count)
echo $((TMP + 1)) >count
rm -f lock
