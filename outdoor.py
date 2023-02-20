#!/usr/bin/python

from mininet.node import OVSKernelSwitch, Host
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from subprocess import call


def myNetwork():

    net = Mininet_wifi(topo=None,
                       build=False,
                       link=wmediumd,
                       wmediumd_mode=interference,
                       ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', position='131.0,134.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', position='97.0,464.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='1', mode='g', position='438.0,363.0,0')
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid',
                             channel='1', mode='g', position='442.0,133.0,0')
    ap5 = net.addAccessPoint('ap5', cls=OVSKernelAP, ssid='ap5-ssid',
                             channel='1', mode='g', position='727.0,182.0,0')
    ap6 = net.addAccessPoint('ap6', cls=OVSKernelAP, ssid='ap6-ssid',
                             channel='1', mode='g', position='717.0,446.0,0')
    ap7 = net.addAccessPoint('ap7', cls=OVSKernelAP, ssid='ap7-ssid',
                             channel='1', mode='g', position='907.0,278.0,0')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    info( '*** Add hosts/stations\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    sta1 = net.addStation('sta1', ip='10.0.0.1',
                           position='68.0,561.0,0')
    sta2 = net.addStation('sta2', ip='10.0.0.2',
                           position='59.0,239.0,0')
    sta3 = net.addStation('sta3', ip='10.0.0.3',
                           position='231.0,250.0,0')
    sta4 = net.addStation('sta4', ip='10.0.0.4',
                           position='540.0,403.0,0')
    sta5 = net.addStation('sta5', ip='10.0.0.5',
                           position='468.0,247.0,0')
    sta6 = net.addStation('sta6', ip='10.0.0.6',
                           position='693.0,280.0,0')
    sta7 = net.addStation('sta7', ip='10.0.0.7',
                           position='877.0,361.0,0')
    sta8 = net.addStation('sta8', ip='10.0.0.8',
                           position='797.0,552.0,0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info( '*** Add links\n')
    net.addLink(ap1, s1)
    net.addLink(ap2, s1)
    net.addLink(ap3, s1)
    net.addLink(ap4, s1)
    net.addLink(ap5, s2)
    net.addLink(ap6, s2)
    net.addLink(ap7, s2)
    net.addLink(sta7, ap7)
    net.addLink(sta8, ap6)
    net.addLink(sta6, ap5)
    net.addLink(sta4, ap3)
    net.addLink(sta5, ap4)
    net.addLink(sta3, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta1, ap2)
    net.addLink(s1, s3)
    net.addLink(s2, s3)
    net.addLink(s3, h1)

    net.plotGraph(max_x=1000, max_y=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('ap1').start([])
    net.get('ap2').start([])
    net.get('ap3').start([])
    net.get('ap4').start([])
    net.get('ap5').start([])
    net.get('ap6').start([])
    net.get('ap7').start([])
    net.get('s1').start([])
    net.get('s2').start([])
    net.get('s3').start([])

    info( '*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

