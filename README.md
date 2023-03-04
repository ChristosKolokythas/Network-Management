# Mininet
Mininet is a network simulation tool that allows you to create network simulation
create virtual SDN networks. Mininet-WIFI is a fork of mininet that
provides us with additional tools to visualize the network we are designing such as
Miniedit. For the implementation of the following topologies the tool
Miniedit in Linux environment.
### Mininet Topologies
For the simulation of the indoor and outdoor scenarios we relied on the topologies that
described in the project. In both cases the host
represents the network server which communicates with the antennas, which
represented by the access points, through the switches.
For the network of the outdoor scenario we used 7 access points (ap), 3 switches and 1
host. Also for the simulation of the users we used 8 statios (sta). In
normal conditions the number of users would be different but due to the
limitations of the program we used 8 as an indication.

For the indoor network we used 4 access points, 1 switch and 1 host. Here
we used 1 station representing a user who is located in the space of the
office.

### Fault Management

The term "Fault Management" describes the
sequence of our operations to detect, isolate and repair
problems in a network. For Fault Management on the networks we created,
through continuous monitoring of the network we can identify the fault
(in this case the loss of an antenna) and through network reordering
we can isolate and repair it.

The simulation of the loss is done through commands from the terminal at runtime. By
py ap.stop_() command to simulate the loss of an antenna. Then with
using py net.addLink() we reconfigure the network to isolate the loss
and resume operation. Finally, for users who are outside the network
range due to the antenna failure we simulate their movement with
using py sta.setPosition().

# Smart Evacuation
For a detailed presentation of the mockups you can open the pdf file and find the Smart Evacuation section

# Thingsboard
### Description of the operation
For the external scenario in which we are located in the University City
we created 7 assets which represent the antennas and 7 devices which
are heat detection sensors each one of which corresponds to one of the devices.
asset. To simulate the data that the sensors detect
we created a generator which generates random values every 30 minutes
seconds and generates values from 30 to 70 degrees Celsius. For the dashboard
we used the map widget provided by thingsboard. The alarms
were set to activate if the temperature exceeds
60 degrees Celsius.

For the indoor scenario we created a building that contains all the
the thermostats and placed them on an image map. The procedure for
to create the sensors and alarms is the same as in the outdoor scenario. Screenshots from the operation of thingsboard can be found in the pdf file.

##### Authors
Kolokythas Christos
Themistoklis Sotiropoulos
