#!/usr/bin/env python
# -*- coding: utf-8 -*-
import read_json
import write_json

#判断是否为数字的函数
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

#主要程序部分
print ("当前AlterId为：%s") % str(readjson.ConfAlterId)
print ("请输入新的AlterId：")
newalterId=raw_input()
if (is_number(alterId)):
    writejson.WriteAlterId(newalterId)
    print("AlterId修改成功！")
else:
    print ("输入错误，请检查是否为数字")
