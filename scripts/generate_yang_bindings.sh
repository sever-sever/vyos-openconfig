#!/bin/sh

PYANG_CMD="pyang --plugindir /usr/lib/python3.11/site-packages/pyangbind/plugin/ --format pybind -o"

generate_bindings() {
    $PYANG_CMD ../oc_bgp.py openconfig-bgp.yang
    $PYANG_CMD ../oc_system.py openconfig-system.yang
    $PYANG_CMD ../oc_network_instance.py openconfig-network-instance.yang
    $PYANG_CMD ../oc_interfaces.py openconfig-interfaces.yang
    $PYANG_CMD ../oc_local_routing.py openconfig-local-routing.yang
}

generate_bindings
