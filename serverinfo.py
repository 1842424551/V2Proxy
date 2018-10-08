#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import urllib2
import base64
import json
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
    mystreamsecurity="TLS      ：开启\n"
else:
    mystreamsecurity="TLS      ：关闭\n"

#输出信息
print("\nIP       ：%s") % str(myip)
print("Port     ：%s") % str(readjson.ConfPort)
print("UUID     ：%s") % str(readjson.ConfUUID)
print("AlterId  ：%s") % str(readjson.ConfAlterId)
print("Security ：%s") % str(readjson.ConfSecurity)
print("Network  ：%s") % str(mystreamnetwork)
print("%s") % str(mystreamsecurity)

for index, sin_user_conf in enumerate(readjson.multiUserConf):
    index += 1
    protocol=sin_user_conf["protocol"]
    print("%d." % index)
    print("Group: %s" % sin_user_conf["indexDict"]["group"])
    print("IP：%s" % sin_user_conf["add"]) 
    print("Port：%s" % sin_user_conf["port"])
    if sin_user_conf["email"]:
        if protocol == "vmess" or protocol == "mtproto" or protocol == "shadowsocks":
            print("Email: %s" % sin_user_conf["email"])
        elif protocol == "socks":
            print("User: %s" % sin_user_conf["email"])
    if protocol == "vmess":
        print("UUID：%s" % sin_user_conf["id"])
        print("Alter ID: %s" % sin_user_conf["aid"])
        if sin_user_conf["net"] == "h2":
            print("Network：%s" % ("HTTP/2  伪装Path: " + sin_user_conf["path"])) 
        elif sin_user_conf["net"] == "ws":
            print("Network：%s" % ("WebSocket  伪装Host: " + sin_user_conf["host"] + " 伪装Path: " + sin_user_conf["path"])) 
        else:
            print("Network：%s" % (sin_user_conf["net"] + " " + sin_user_conf["type"])) 
        print("TLS: %s" % ("关闭" if sin_user_conf["tls"] == "" else "开启"))

copy_conf = sin_user_conf.copy()
base64_str = base64.b64encode(bytes(json.dumps(copy_conf), 'utf-8'))
share_url = "vmess://" + bytes.decode(base64_str) 
#绿色字体显示
print("\033[32m")
print(share_url)
print("\033[0m")
print("")
