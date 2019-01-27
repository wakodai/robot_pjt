# -*- coding:utf-8 -*-
# python 2
import serial
import socket

host = "192.168.0.9" #お使いのサーバーのホスト名を入れます
port = 49152 #適当なPORTを指定してあげます
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#client.connect((host, port)) #これでサーバーに接続します

ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=None)

while True:
    #line = ser.readline()
    recv = ser.read(2) #recv is str
    #print(type(recv))
    #print(line.rstrip())
    ####print(recv)
    #client.send(line.rstrip())
    #client.send(recv)
    client.sendto(recv, (host, port))
ser.close()
