#!/bin/bash

for file in $(ls input); do
    python3 fancy.py input/$file > "${file##*/}"_op.txt;
done
