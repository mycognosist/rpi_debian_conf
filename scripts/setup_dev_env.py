# setup_dev_env.py

# Install and configure development environment for PeachCloud on RPi3 with Debian Buster
# Includes installation of Rust and setup of I2C and a RTC
# Consult the PeachCloud GPIO documentation [ ... ] for pinouts

import os
import subprocess
import sys


# Save arguments
username = sys.argv[1]

# Update Pi and install requirements
subprocess.call(["apt-get","update", "-y"])
subprocess.call(["apt-get","upgrade", "-y"])
subprocess.call(["apt-get","install", "vim", "man-db", "locales", "iw", "hostapd", "dnsmasq", "git", "python-smbus", "i2c-tools", "build-essential", "curl", "sudo", "-y"])
subprocess.call(["/usr/sbin/adduser", username])

# Overwrite configuration files
subprocess.call(["cp", "conf/interfaces", "/etc/network/interfaces"])
subprocess.call(["cp", "conf/hostapd", "/etc/default/hostapd"])
subprocess.call(["cp", "conf/hostapd.conf", "/etc/hostapd/hostapd.conf"])
subprocess.call(["cp", "conf/dnsmasq.conf", "/etc/dnsmasq.conf"])
subprocess.call(["cp", "conf/dhcpd.conf", "/etc/dhcpd.conf"])
subprocess.call(["cp", "conf/00-accesspoint.rules", "/etc/udev/rules.d/00-accesspoint.rules"])
subprocess.call(["cp", "conf/activate-rtc.service", "/etc/systemd/system/activate-rtc.service"])

# left out: setting of locales, rust installation, console log-level printing
