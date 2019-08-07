# Collapse access point and start wlan0
systemctl stop hostapd
systemctl stop dnsmasq
ifup wlan0
#iw dev ap0 del
#ip link set ap0 down
