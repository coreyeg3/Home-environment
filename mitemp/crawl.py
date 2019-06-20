#!/usr/bin/env python3

from btlewrap.bluepy import BluepyBackend
from mitemp_bt.mitemp_bt_poller import MiTempBtPoller, \
            MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY
from influxdb import InfluxDBClient
import time
import os
import csv


f=open('Crawl.txt','a+')

crawl = '4c:65:a8:dd:55:8f'
cpoller = MiTempBtPoller(crawl, BluepyBackend)
crawl_temp = cpoller.parameter_value(MI_TEMPERATURE)
crawl_hum = cpoller.parameter_value(MI_HUMIDITY)
crawl_bat = cpoller.parameter_value(MI_BATTERY)
f.write('{0},{1},{2}\n'.format(crawl_temp,crawl_hum,crawl_bat))
time.sleep(1)

f.close()


rows = csv.reader(open('Crawl.txt', newline='\n'), delimiter=',')
for row in rows:
    row=row
crawl_temp=float(row[0])
crawl_hum=float(row[1])
crawl_bat=int(row[2])

json_body = [
{
    "measurement": "Environment",
    "tags": {
        "host": "raspberry"
    },
    "fields":{
            "Crawl Space Temperature": float(crawl_temp),
            "Crawl Space Humidity": float(crawl_hum),
            "Crawl Space Battery": crawl_bat,
        }
}
]
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client .switch_database('environment')
client .write_points(json_body)

