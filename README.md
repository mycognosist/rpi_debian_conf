# rpi_debian_conf

Configuration instructions, files and scripts for deploying Debian Buster to a Raspberry Pi 3.

_Work in progress._

**Network**

In this configuration, the RPi connects to other networks with the `wlan0` interface and deploys an access point on the `ap0` interface. Only one of these modes is active at a time (client or access point).

Networking is handled with `wpa_supplicant`, `hostapd` and `dnsmasq`.

### Prerequisite Steps

Download the latest Debian Buster preview image for RPi3 and flash it to an SD card (card is located at `/dev/mmcblk0` in this case):

`wget https://people.debian.org/~gwolf/raspberrypi3/20190628/20190628_raspberry-pi-3_buster_PREVIEW.img.xz`
`xzcat 20190628_raspberry-pi-3_buster_PREVIEW.img.xz | sudo dd of=/dev/mmcblk0 bs=64k oflag=dsync status=progress`

### Setup

All setup commands are detailed in `COMMANDS.md`.

Quick setup commands to connect to a local WiFi network over the `wlan0` interface (assuming `eth0` connection is not possible):

`root`
`raspberry`
`ip link set wlan0 up`
`wpa_passphrase <SSID> <PASS> > /etc/wpa_supplicant/wpa_supplicant.conf`
`nano /etc/wpa_supplicant/wpa_supplicant.conf`

[ Add the following two lines to top of file ]

`ctrl_interface=/run/wpa_supplicant`
`update_config=1`

[ Save and exit ]

nano /etc/network/interfaces

[ Add the following lines to the file ]

`auto lo`
`iface lo inet loopback`

`allow-hotplug wlan0`
`auto wlan0`
`iface wlan0 inet dhcp`
`    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf`

[ Save and exit ]

`reboot now`

[ Pi should now be connected to the WiFi network 
]
### Scripts

Includes `deploy_client.sh` and `deploy_ap.sh`. These two scripts allow easy switching between client and access point modes.

The `setup_dev_env.py` script can be executed once your Pi is internet-connected. It takes <USER> and <PASS> arguments to create a new system user. The script will install system requirements and copy configuration files relating to networking, I2C and RTC.

_TODO: Add flags to (de)select I2C, RTC and Rust install & config._

`git clone https://github.com/mycognosist/rpi_debian_conf.git`
`cd rpi_debian_conf`
`python setup_dev_env.py <USER> <PASS>`

**IMPORTANT: Please do not forget to set a new password for the root user!**
