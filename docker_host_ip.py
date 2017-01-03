import logging
import os
import re


def get_ip_within_host():
    cmd = os.popen("/sbin/ip")
    returns = cmd.readall()
    regex = r"/default via ((?:[0-9]{1,3}\.){3}[0-9]{1,3}) dev eth0/"
    return re.findall(regex, returns)


def _get_ifconfig(interface_name):
    cmd = os.popen("ifconfig %s" % interface_name)
    return cmd.read()


def get_docker_host_ip(iface_name="docker0"):
    """
    Only work while docker0 exists
    :return:
    """
    returns = _get_ifconfig(iface_name)
    regex = r"inet\ addr:((\d{1,3}\.){1,3}\d{1,3})"
    matched = re.findall(regex, returns)
    try:
        return matched[0][0]
    except IndexError:
        logging.exception("Failed to get docker0's ip address, check if it exists.")
        return None
