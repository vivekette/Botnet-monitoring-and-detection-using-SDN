# Botnet-monitoring-and-detection-using-SDN


PFE TELECOM SUDPARIS 2016
Mehdi Mtimet and Geoffrey Boulanger, directed by Gregory Blanc

# Subject

Botnet monitoring and detection using Software Defined Networking. Mininet topology using POX Controller to manage flows between hosts.

# How to use

To initialize the Mininet topology, open a command prompt on your Mininet Virtual Machine and enter

```
sudo mn --custom init_topology.py --topo mytopo --mac --switch ovsk --controlle remote
```

Then, you can start the controller controller_pox.py

The 3 scripts describe how a bot master and his slaves behave compared to a sane client.
You can launch them by opening an xterm terminal in your Mininet VM

```
xterm Client
xterm Slave
xterm Master
```

and execute each corresponding script.
