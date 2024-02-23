# PROBADO LA SEMANA PASADA
import requests
from requests.auth import HTTPBasicAuth

controller_ip = '192.168.18.21'
username = 'admin'
password = 'admin'

node_id = 'openflow:968934587319'#'openflow:4'
port_number1 = 'openflow:968934587319:2' #openflow:4294976775:2
port_number2 = 'openflow:968934587319:3'
vlan_id = '400'
id_flow1_port1='89-400-e1'
id_flow2_port2='89-400-e2'

url1 = f'http://{controller_ip}:8181/restconf/config/opendaylight-inventory:nodes/node/{node_id}/table/0/flow/{id_flow1_port1}'
url2 = f'http://{controller_ip}:8181/restconf/config/opendaylight-inventory:nodes/node/{node_id}/table/0/flow/{id_flow2_port2}'


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
flowp2={
    "flow": [
            {
                "table_id": 0,
                "id": id_flow2_port2,
                "priority": 1145,
                "hard-timeout": 0,
                "idle-timeout": 0,
                "match": {
                    "in-port": port_number2,
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
response_vlanp2 = requests.put(url2, json=flowp2, auth=HTTPBasicAuth(username, password))

if response_vlanp1.status_code == 200 and response_vlanp2.status_code == 200:
    print('VLAN agregada con éxito')
else:
    print('Error al agregar VLAN')