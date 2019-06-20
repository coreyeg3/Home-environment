#!/usr/bin/env python3

from btlewrap.bluepy import BluepyBackend
from mitemp_bt.mitemp_bt_poller import MiTempBtPoller, \
            MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY
from influxdb import InfluxDBClient
import time
import os
import csv


f=open('Kitchen.txt','a+')

kitchen = '4c:65:a8:dc:1f:e3'
kitpoller = MiTempBtPoller(kitchen, BluepyBackend)
kit_temp = kitpoller.parameter_value(MI_TEMPERATURE)
kit_hum = kitpoller.parameter_value(MI_HUMIDITY)
kit_bat = kitpoller.parameter_value(MI_BATTERY)
f.write('{0},{1},{2}\n'.format(kit_temp,kit_hum,kit_bat))
time.sleep(1)
f.close()


rows = csv.reader(open('Kitchen.txt', newline='\n'), delimiter=',')
for row in rows:
    row=row

kit_temp=float(row[0])
kit_hum=float(row[1])
kit_bat=int(row[2])

json_body = [
{
    "measurement": "Environment",
    "tags": {
        "host": "raspberry"
    },
    "fields":{
            "Kitchen Humidity": float(kit_hum),
            "Kitchen Temperature": float(kit_temp),
            "Kitchen Battery": kit_bat,
        }
}
]
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client .switch_database('environment')
client .write_points(json_body)

