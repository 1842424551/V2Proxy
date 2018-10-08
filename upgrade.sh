#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

#重装V2Proxy
rm -rf /usr/local/V2Proxy
cd /usr/local/
git clone https://github.com/MaruKoh/V2Proxy
cd /usr/local/V2Proxy/
chmod +x *.py

#重装操作菜单
rm -rf /usr/local/bin/v2ray
cp /usr/local/V2Proxy/v2ray /usr/local/bin/
chmod +x /usr/local/bin/v2ray

#更新v2ray主程序
bash <(curl -L -s https://install.direct/go.sh)

clear
echo "脚本已更新！"
