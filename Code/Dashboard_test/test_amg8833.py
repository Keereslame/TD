import time
import busio
import board
import adafruit_amg88xx
import numpy as np
from influxdb import InfluxDBClient
import time



#print("Local time:", local_time)
 
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

client = InfluxDBClient(host='localhost', port=8086)

max = 0
min = 0
 
while True:
    # seconds passed since epoch
    seconds = time.time()
    #print(seconds)
    #print(int(seconds))
    ns = seconds * (1000000000.0)
    #print(ns)
    local_time = time.ctime(seconds)
    #print(local_time)
    values = []
    json_body = []
    sendData = False
    for row in amg.pixels:
        value = []
        # Pad to 1 decimal place
        #print(["{0:.1f}".format(temp) for temp in row])
        #print("")
        for temp in row:
            value.append(temp)
        #print(value)
        if value[0] == 0:
            break
        values.append(value)
    #print(values)
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
    #print("max =")
    #print(max)
    #print("min =")
    #print(min)
    #print("\n")
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
    #print(sendData)
    time.sleep(300)
    