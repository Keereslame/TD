#The base come frome https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/python-circuitpython
import time
import busio
import board
import adafruit_amg88xx
import numpy as np
from influxdb import InfluxDBClient
import time

 
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

client = InfluxDBClient(host='localhost', port=8086)

max = 0
min = 0
 
while True:
    # seconds passed since epoch
    seconds = time.time()
    ns = seconds * (1000000000.0)
    local_time = time.ctime(seconds)
    values = []
    json_body = []
    sendData = False
    for row in amg.pixels:
        value = []
        for temp in row:
            value.append(temp)
        if value[0] == 0:
            break
        values.append(value)
    if len(values) != 0:
        max_temp = values[0][0]
        min_temp = values[0][0] 
        for i in values:
            for j in i:
                if j > max_temp:
                    max_temp = j
                if j< min_temp:
                    min_temp = j
        max = max_temp
        min = min_temp
        json_body = [
        {
            "measurement": "amg8833",
            "tags": {
            },
            #"time": int(seconds)-7200,
            "fields": {
                "temp_max": max,
                "temp_min": min
            }
        }
        ]
    if len(json_body) != 0:
        sendData = client.write_points(json_body, 'n', 'lowimpact_food')
    time.sleep(5)
    