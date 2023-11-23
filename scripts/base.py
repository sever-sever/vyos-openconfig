#!/usr/bin/env python3

from oc_interfaces import openconfig_interfaces
from oc_local_routing import openconfig_local_routing
from oc_system import openconfig_system
from oc_network_instance import openconfig_network_instance

import pyangbind.lib.pybindJSON as pybindJSON
from pyangbind.lib.serialise import pybindIETFXMLEncoder

# Define modules
oc_interfaces = openconfig_interfaces()
oc_local_routing = openconfig_local_routing()
oc_system = openconfig_system()
oc_network_instance = openconfig_network_instance()


# Add network instance 'default'
oc_network_instance.network_instances.network_instance.add('default')
oc_network_instance.network_instances.network_instance.get()
oc_network_instance.get()

tmp = oc_network_instance.network_instances.network_instance.get()

print(pybindJSON.dumps(tmp, mode="ietf"))
print(pybindIETFXMLEncoder.serialise(oc_network_instance))


# Add interface 'eth0'
oc_interfaces.interfaces.interface.add('eth0')

tmp = oc_interfaces.get()

# RFC7951-formatted JSON
print(pybindJSON.dumps(tmp, mode="ietf"))
print(pybindIETFXMLEncoder.serialise(oc_network_instance))
