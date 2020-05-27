# Deploy access point on ap0
systemctl stop wpa_supplicant
ifdown wlan0
systemctl unmask hostapd
systemctl start hostapd
systemctl start dnsmasq
ip link set ap0 up
