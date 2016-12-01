import mock

import docker_host_ip as dhi


ifconfig_out = """
    docker0   Link encap:Ethernet  HWaddr 02:42:29:bd:f4:cf
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::42:29ff:febd:f4cf/64 Scope:Link
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:43759 errors:0 dropped:0 overruns:0 frame:0
          TX packets:44987 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:1978932 (1.9 MB)  TX bytes:475173168 (475.1 MB)

"""


def test_get_docker_host_ip():
    with mock.patch.object(
        dhi,
        "_get_ifconfig",
    ) as mocked_ifconfig:
        mocked_ifconfig.return_value = ifconfig_out
        out = dhi.get_docker_host_ip()
        assert out == "172.17.0.1"


