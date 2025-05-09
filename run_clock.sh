#!/bin/bash
export DISPLAY=:0
while true;do
    if xdpyinfo > /dev/null;then
        break
    fi
    sleep 1
done


while true
do
    # 检测8123端口是否开放
    nc -z 127.0.0.1 8123 > /dev/null 2>&1
    
    # 检查上一条命令的退出状态
    if [ $? -eq 0 ]; then
        cd /home/pi/clock-pyqt/src
        python main.py
    fi
    sleep 1
    
    
done