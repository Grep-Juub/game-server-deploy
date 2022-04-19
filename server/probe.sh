#!/usr/bin/env bash

RUNNING=$(lsof -i -P -n | grep 7778 | wc -l)

if [[ $RUNNING  -eq "1" ]]
then
        exit 0
else
        exit 1
fi
