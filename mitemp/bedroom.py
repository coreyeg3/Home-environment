#!/usr/bin/env python3

from btlewrap.bluepy import BluepyBackend
from mitemp_bt.mitemp_bt_poller import MiTempBtPoller, \
            MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY
from influxdb import InfluxDBClient
import time
import os
import csv


f=open('Bedroom.txt','a+')

bedroom = '4c:65:a8:dd:54:04'
poller = MiTempBtPoller(bedroom, BluepyBackend)
bed_temp = poller.parameter_value(MI_TEMPERATURE)
bed_hum = poller.parameter_value(MI_HUMIDITY)
bed_bat = poller.parameter_value(MI_BATTERY)
f.write('{0},{1},{2}\n'.format(bed_temp,bed_hum,bed_bat))
time.sleep(1)
f.close()

rows = csv.reader(open('Bedroom.txt', newline='\n'), delimiter=',')
for row in rows:
    row=row

bed_temp=float(row[0])
bed_hum=float(row[1])
bed_bat=int(row[2])

json_body = [
{
    "measurement": "Environment",
    "tags": {
        "host": "raspberry"
    },
    "fields":{
            "Bedroom Temperature": float(bed_temp),
            "Bedroom Humidity": float(bed_hum),
            "Bedroom Battery": bed_bat,

        }
}
]
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client .switch_database('environment')
client .write_points(json_body)





   