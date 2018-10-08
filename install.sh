#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

#检查是否为Root
[ $(id -u) != "0" ] && { echo "Error: You must be root to run this script"; exit 1; }

#检查系统信息
if [ -f /etc/redhat-release ];then
        OS='CentOS'
    elif [ ! -z "`cat /etc/issue | grep bian`" ];then
        OS='Debian'
    elif [ ! -z "`cat /etc/issue | grep Ubuntu`" ];then
        OS='Ubuntu'
    else
        echo "Not support OS, Please reinstall OS and retry!"
        exit 1
fi

#禁用SELinux
if [ -s /etc/selinux/config ] && grep 'SELINUX=enforcing' /etc/selinux/config; then
    sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
    setenforce 0
fi

#安装依赖
if [[ ${OS} == 'CentOS' ]];then
	yum install curl wget unzip git ntp ntpdate lrzsz python socat -y
else
	apt-get update
	apt-get install curl unzip git ntp wget ntpdate python socat lrzsz -y
fi

#安装 acme.sh 以自动获取SSL证书
curl  https://get.acme.sh | sh


#克隆V2Proxy项目
cd /usr/local/
rm -R V2Proxy
git clone https://github.com/MaruKoh/V2Proxy

#安装V2ray主程序
bash <(curl -L -s https://install.direct/go.sh)

#配置V2ray初始环境
cp /usr/local/V2Proxy/v2ray /usr/local/bin
chmod +x /usr/bin/v2ray
chmod +x /usr/local/bin/v2ray
rm -rf /etc/v2ray/config.json
mv /usr/local/V2Proxy/json_template/server.json /etc/v2ray/config.json
UUID=$(cat /proc/sys/kernel/random/uuid)
sed -i "s/cc4f8d5b-967b-4557-a4b6-bde92965bc27/${UUID}/g" /etc/v2ray/config.json
python /usr/local/V2Proxy/genclient.py
python /usr/local/V2Proxy/openport.py
service v2ray restart


clear
echo "V2Ray配置信息:"
#直接显示v2ray安装后的配置信息
python /usr/local/V2Proxy/serverinfo.py

echo "V2Proxy v1.0 安装成功！By: 南音"
echo "输入 v2ray 回车即可使用"
