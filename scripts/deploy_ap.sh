# Deploy access point on ap0
systemctl stop wpa_supplicant
ifdown wlan0
systemctl start hostapd
systemctl start dnsmasq
