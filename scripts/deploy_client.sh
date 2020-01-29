# Collapse access point and start wlan0
systemctl stop hostapd
systemctl stop dnsmasq
ifup wlan0
