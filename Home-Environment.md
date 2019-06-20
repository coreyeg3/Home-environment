## Docker Install

```c
sudo apt-get update
curl -sSL https://get.docker.com | sh

docker run \
>   -d \
>   -p 3000:3000 \
>   --name=grafana \
>   grafana/grafana
```

## Python Configuration

```c
sudo apt install python3-pip 
pip3 install influxdb
pip3 install bluepy
```

## Setup & install InfluxDB

Follow install guide here: [InfluxDB Docs](<https://docs.influxdata.com/influxdb/v1.7/introduction/installation/>)

```c
root@raspberrypi:/home/pi# influx
Connected to http://localhost:8086 version 1.7.6
InfluxDB shell version: 1.7.6
Enter an InfluxQL query
> CREATE DATABASE environment
> USE environment
Using database environment
> quit
root@raspberrypi:/home/pi#
```

