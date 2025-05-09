# clock-pyqt
用pyqt编写的一个时钟


# 部署到核桃派box上
使用硬件为walnutpi-box小主机，烧录官方的带桌面且预装了hass的镜像 **2024-7-12_V2.4.0_WalnutPi-1B_6.1.31_Home-Assistant_deaktop**

1. 安装python库
```
sudo pip install requests
```
2. 修改系统时区
```
sudo timedatectl set-timezone Asia/Shanghai
```