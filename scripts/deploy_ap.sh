# Stop wlan0 and deploy access point on ap0
systemctl stop wpa_supplicant
ifdown wlan0
systemctl start hostapd
systemctl start dnsmasq
