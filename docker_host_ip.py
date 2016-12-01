import os
import re


def get_ip_within_host():
    cmd = os.popen("/sbin/ip")
    returns = cmd.readall()
    regex = r"/default via ((?:[0-9]{1,3}\.){3}[0-9]{1,3}) dev eth0/"
    return re.findall(regex, returns)


def _get_ifconfig():
    cmd = os.popen("ifconfig docker0")
    return cmd.readall()


def get_docker_host_ip():
    """
    Only work while docker0 exists
    :return:
    """
    returns = _get_ifconfig()
    regex = r"inet\ addr:((\d{1,3}\.){1,3}\d{1,3})"
    matched = re.findall(regex, returns)
    return matched[0][0]
