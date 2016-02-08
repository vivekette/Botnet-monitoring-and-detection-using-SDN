#!/usr/bin/python

## (c) Mehdi Mtimet and Geoffrey Boulanger 
## PFE - Monitoring de botnets a travers des reseaux SDN
## 2015 - 2016

from mininet.topo import Topo
from mininet.net import Mininet

class MyTopo( Topo ):
    

    def __init__( self ):
        

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Client = self.addHost( 'client' )
	Master = self.addHost( 'master' )
	Slave = self.addHost( 'slave' )
	Sinkhole = self.addHost( 'sinkhole' )
		
        Switch = self.addSwitch( 's1' )
        

        # Add links
        self.addLink( Client, Switch )
	self.addLink( Master, Switch )
	self.addLink( Slave, Switch )
	self.addLink( Sinkhole, Switch )

topos = { 'mytopo': ( lambda: MyTopo() ) }
