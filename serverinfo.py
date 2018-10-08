#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import urllib2
import base64
#获取本机IP地址
myip = urllib2.urlopen('http://api.ipify.org').read()
myip = myip.strip()

#判断传输配置
mystreamnetwork=str(readjson.ConfStreamNetwork)

if readjson.ConfStreamNetwork=="kcp" :
    if(readjson.ConfStreamHeader=="utp"):
        mystreamnetwork="mKCP 伪装 BT下载流量"
    elif(readjson.ConfStreamHeader=="srtp"):
        mystreamnetwork="mKCP 伪装 FaceTime通话"
    elif(readjson.ConfStreamHeader=="wechat-video"):
        mystreamnetwork="mKCP 伪装 微信视频流量"
    else:
        mystreamnetwork="mKCP"
elif readjson.ConfStreamNetwork=="http":
    mystreamnetwork="HTTP伪装"
elif readjson.ConfStreamNetwork=="ws":
    mystreamnetwork="WebSocket"

if (readjson.ConfStreamSecurity=="tls"):
    mystreamsecurity="TLS      ：开启"
else:
    mystreamsecurity="TLS      ：关闭"

#输出信息
print("\nIP       ：%s") % str(myip)
print("Port     ：%s") % str(readjson.ConfPort)
print("UUID     ：%s") % str(readjson.ConfUUID)
print("AlterId  ：%s") % str(readjson.ConfAlterId)
print("Security ：%s") % str(readjson.ConfSecurity)
print("Network  ：%s") % str(mystreamnetwork)
print("%s") % str(mystreamsecurity)
