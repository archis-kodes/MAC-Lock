import uuid
import serial
import time
import platform
import re
import subprocess
import serial.tools.list_ports

#for getting MAC address
def get_primary_mac_address():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = ':'.join(mac_num[i:i+2] for i in range(0, 12, 2))
    return mac

#for finding PORT of Arduino
def find_arduino_port():
    arduino_ports = []
    ports = serial.tools.list_ports.comports()
    
    for port, desc, hwid in sorted(ports):
        if 'Arduino Uno' in desc or 'Arduino/Genuino Uno' in desc:
            arduino_ports.append(port)
    
    return arduino_ports

if __name__ == "__main__":
    #checks for PORT of Arduino
    arduino_ports = find_arduino_port()
    if arduino_ports:
        for port in arduino_ports:
            print('ok')
            UNOport=port

        #checks for MAC Address        
        mac_address = get_primary_mac_address()
arduino = serial.Serial(UNOport, 9600, timeout=1)
time.sleep(2)
arduino.write((mac_address + '\n').encode())
arduino.close()

