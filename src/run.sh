#!/bin/sh

if [ -f $1 ]; then \
	export PYTHONPATH=$PWD;
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/../bin;
	export LDC_PATH=$PWD/..
	python main.py
else \
	echo "File not found! ($1)";
fi
