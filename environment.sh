#!/bin/bash


while true
do
	until python3 /home/pi/mitemp/kitchen.py &>> logfiles/kit.txt; do
		sleep 1
	done

	until python3 /home/pi/mitemp/crawl.py &>> logfiles/crawl.txt; do
		sleep 1
	done

	until python3 /home/pi/mitemp/bedroom.py &>> logfiles/bed.txt; do
		sleep 1
	done
done
