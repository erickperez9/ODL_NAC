# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:26:45 2023

@author: Mateo
"""

import requests
from requests.auth import HTTPBasicAuth

def asigna_vlan(controller_ip, username, password, node_id, port_number1, mac, usuario, departamento, vlan_id):
    id_flow1_port1=usuario+'-'+departamento+'-'+vlan_id
    url1 = f'http://{controller_ip}:8181/restconf/config/opendaylight-inventory:nodes/node/{node_id}/table/0/flow/{id_flow1_port1}'
    flowp1={
        "flow": [
                {
                    "table_id": 0,
                    "id": id_flow1_port1,
                    "priority": 1145,
                    "hard-timeout": 0,
                    "idle-timeout": 0,
                    "match": {
                        "in-port": port_number1,
                        "vlan-match": {
                            "vlan-id": {
                                "vlan-id": vlan_id,
                                "vlan-id-present": "true"
                            }
                        }
                    },
                    "instructions": {
                        "instruction": [
                            {
                                "order": 0,
                                "apply-actions": {
                                    "action": [
                                        {
                                            "order": 0,
                                            "push-vlan-action": {
                                                "ethernet-type": 33024,
                                                "tag": vlan_id,
                                                "pcp": 7,
                                                "cfi": 0,
                                                "vlan-id": vlan_id
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
    
    }
    
    
    response_vlanp1 = requests.put(url1, json=flowp1, auth=HTTPBasicAuth(username, password))
    
    
    if response_vlanp1.status_code == 200:
        print(f'VLAN {id_flow1_port1} agregada con éxito')
        
    else:
        print(f'Error al agregar VLAN {id_flow1_port1}')