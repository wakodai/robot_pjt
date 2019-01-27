# -*- coding:utf-8 -*-
# python 3

import socket
import numpy as np
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

host = "192.168.0.9" #お使いのサーバーのホスト名を入れます
port = 49152 #クライアントと同じPORTをしてあげます

#serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします
#serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）

#graph
fig, ax = plt.subplots(1,1)
#x = np.arange(-np.pi, np.pi, 0.1)
#y = np.sin(x)
x = np.arange(0,10,1)
y = np.arange(0,10,1)
lines, = ax.plot(x, y)


print ('Waiting for connections...')
#clientsock, client_address = serversock.accept() #接続されればデータを格納

i = 0


while True:

    #この時点ではbyte型
#    rcvmsg = clientsock.recv(1024)
    rcvmsg = serversock.recv(1024)
#    print (type(rcvmsg)) # rcvmsg is bytes type
    # decode()でbyte型からstr型へ変換
    #rcvmsg_str = rcvmsg.decode()
    hoge = int.from_bytes(rcvmsg, 'little')
#    print (type(hoge))
    print (hoge)
#    print ('str %s' % (rcvmsg_str))
#    print (type(rcvmsg_str))
#    rcvmsg_int = int(rcvmsg_str)
#    print ('int %d' % (rcvmsg_int))
#    print (type(rcvmsg_int))

    x += 1
#    y = hoge
    y = np.roll(y,-1)
    y[-1] = hoge

    lines.set_data(x, y)
    #print(x,y)

    ax.set_xlim((x.min(), x.max()))
#    ax.set_ylim([0,20])
    ax.set_ylim((x.min(), y.max()*2))

    plt.pause(.01) #sec


    if rcvmsg == '':
      break
