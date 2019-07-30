# Collapse access point on ap0 and start wlan0
systemctl stop hostapd
systemctl stop dnsmasq
systemctl start wpa_supplicant
ifup wlan0
