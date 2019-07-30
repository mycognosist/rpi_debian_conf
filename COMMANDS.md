[ login ]

root
raspberry
ip link set wlan0 up

[ run previous command again if you get an 'IPv6 not ready' error ]

iwlist wlan0 scan | grep -i ssid
wpa_passphrase SSID PASS > /etc/wpa_supplicant/wpa_supplicant.conf
nano /etc/wpa_supplicant/wpa_supplicant.conf

[ add following two lines to top ]

ctrl_interface=/run/wpa_supplicant
update_config=1

[ save and exit ]

nano /etc/network/interfaces

[ add the following config ]

# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
# source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

allow-hotplug wlan0
auto wlan0
iface wlan0 inet dhcp
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

[ save changes and exit  ]

reboot now

[ login ]

apt-get update && apt-get upgrade -y
apt-get install vim man-db locales iw hostapd dnsmasq sudo -y
nano /etc/locale.gen

[ uncomment # en_US.UTF-8 UTF-8 and save  ]

dpkg-reconfigure locales
adduser glyph
usermod -aG sudo glyph
exit

[ login as new user  ]

sudo vim /etc/default/hostapd

[ uncomment daemon conf and add path  ]

DAEMON_CONF="/etc/hostapd/hostapd.conf"

:wq

sudo vim /etc/hostapd/hostapd.conf

interface=ap0
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
ssid=peach
wpa_passphrase=cloudless

:wq

sudo vim /etc/network/interfaces

[ add the ap0 config  ]

iface ap0 inet static
    address 11.11.11.10
    netmask 255.255.255.0
    network 11.11.11.0
    broadcast 11.11.11.255

:wq

sudo vim /etc/dnsmasq.conf

interface=ap0
listen-address=11.11.11.10
bind-interfaces
server=208.67.222.222
domain-needed
bogus-priv
dhcp-range=11.11.11.11,11.11.11.30,255.255.255.0,24h

:wq

sudo vim /etc/dhcpd.conf

interface ap0
    static ip_address=11.11.11.10/24
    nohook wpa_supplicant

:wq

[ set console logging level ]

sudo sysctl -w kernel.printk="4 4 1 7"

sudo vim /etc/udev/rules.d/00-accesspoint.rules

SUBSYSTEM=="net", ACTION=="add", RUN+="/usr/sbin/iw dev wlan0 interface add ap0 type __ap"
SUBSYSTEM=="net", ACTION=="add", RUN+="/usr/bin/ip address add 11.11.11.10/24 brd + dev ap0"

:wq

sudo reboot now

[ to start access point  ]

sudo systemctl stop wpa_supplicant
sudo ifdown wlan0
sudo systemctl start hostapd
sudo systemctl start dnsmasq

[ to stop access point  ]

sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
sudo systemctl start wpa_supplicant
sudo ifup wlan0
