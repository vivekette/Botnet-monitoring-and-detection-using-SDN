## (c) Mehdi Mtimet and Geoffrey Boulanger 
## PFE - Monitoring de botnets a travers des reseaux SDN
## 2015 - 2016

from pox.core import core
from pox.lib.util import dpidToStr
from pox.lib.addresses import IPAddr, EthAddr
import pox.openflox.libopenflow_01 as of

log = core.getLogger()

class InitPox (object):

    def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

    # Use this table to keep track of which ethernet address is on
    # which switch port (keys are MACs, values are ports).
    self.mac_to_port = {}

    def resend_packet (self, packet_in, out_port):

    msg = of.ofp_packet_out()
    msg.data = packet_in

    # Add an action to send to the specified port
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)

    # Send message to switch
    self.connection.send(msg)

    def filter_packet (self, packet_in, out_port):

    msg = of.ofp_packet_out()
    msg.data = packet_in

    # Parsing the packet for further inspection

    packet = event.parsed
    match = of.ofp_match.from_packet(packet)

    packetToCheck = packet.REQUEST # The thing we are comparing with the signature

    # Create a flow table entry for the packet received

    fm = of.ofp_flow_mod()
    fm.match.in_port = 80 # Checking HTTP requests
    out_port = of.OFPP_NORMAL # Normal port of connection

    # Comparing the packet request to the signature of the botnet

    if packetToCheck.find(signature) != -1: # The signature was found in the packet request
	fm.actions.append(of.ofp_action_output (port = 4)) # Redirect the traffic to another host for further analysing
	fm.actions.append(of.ofp_action_output (port = out_port)) # Send the traffic to the original destination anyway
	self.connection.send(fm) # Send the new entry tables

    # Else, the packet does not match the signature, create the entry table

    else:
	fm.actions.append(of.ofp_action_output(port = out_port))
	self.connection.send(fm)

# Main function to start the module

if __name__ == '__main__':
   InitPox(self.connection)
