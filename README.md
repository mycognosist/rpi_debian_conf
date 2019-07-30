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

### Scripts

Includes `deploy_client.sh` and `deploy_ap.sh`. These two scripts allow easy switching between client and access point modes.
