from bluetooth_battery import BatteryStateQuerier, BatteryQueryError, BluetoothError
import os

def getQueryAndName(line):
    return line[7:24], line[25:]

data = os.popen("bluetoothctl devices").read().split('\n')
for line in data:
    print(line)

deviceChosen = input('Escolha qual aparelho para saber a bateria:\n')

if(len(deviceChosen) < 3):
    query, deviceName = getQueryAndName(data[int(deviceChosen)-1])
else:
    for line in data:
        if deviceChosen in line:
            query, deviceName = getQueryAndName(line)

try:
    query = BatteryStateQuerier(query)
    print(deviceName, "is with", str(query))
    
except BluetoothError as e:
    print(deviceName, "is offline")
except BatteryQueryError as e:
    print(deviceName, "is not supported")