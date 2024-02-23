# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:07:18 2023

@author: PCX
"""

import requests
import json

# Configuración de la solicitud HTTP
controller = "192.168.18.21"
node_id = "openflow:968934587319"
interface_name = "openflow:968934587319:3"
vlan_id = "100"
url = f"http://{controller}:8181/restconf/config/network-topology:network-topology/topology/ovsdb:1/node/{node_id}/ovsdb:interface/{interface_name}/ovsdb:options/ovsdb:interface-option/ovsdb:ofport/ovsdb:ofport-local-vlan-tag={vlan_id}"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic <token de autenticación>'
}

# Configuración de los datos de la solicitud
data = {
    "vlan-tag": vlan_id
}

# Envío de la solicitud PUT para agregar la VLAN al puerto
response = requests.put(url, headers=headers, data=json.dumps(data))

# Verificación de la respuesta de la solicitud
if response.status_code == 200:
    print("La VLAN se agregó correctamente al puerto")
else:
    print("Error al agregar la VLAN al puerto:", response.text)
