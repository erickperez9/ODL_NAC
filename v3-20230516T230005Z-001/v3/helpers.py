# -*- coding: utf-8 -*-
"""
Autores: [Erick Pérez P. - Mateo Molina Y.]
Fecha: [14/06/2023]
Descripcion: [El presente codigo ha sido desarrollado y compilado con la 
              version 3.8 de python. El codigo tiene como objetivo la 
              implementacion de funciones de ayuda para que el servidor NAC
              funcione de manera adecuada. Las funciones son: ordena_macs,
              buscar_usuarios, asigna_departamento, asigna_vlan, crea_matriz,
              put_vlan.]

Licencia: [Este código es de libre distribucion para fines academicos e 
           investigativos.]

"""
import requests
from requests.auth import HTTPBasicAuth

# Ordena las direcciones MAC detectadas en el topologia
def ordena_macs(mac):   
    macs = []
    for i in range(len(mac)):
        macs.append(mac[i][5:])
    return macs

# Valida la existencia de las direcciones MAC detectadas. Tienen como entrada
# las MACs ordenadas y devuelve un vector con los usuarios con en el mismo
# orden que las direcciones MAC
def buscar_usuarios(macs):
    with open("macsDB.txt", "r") as file:
        usuarios_macs = [linea.strip().split() for linea in file]
    resultados = []
    
    for mac in macs:
        for usuario, mac_usuario in usuarios_macs:
            if mac == mac_usuario:
                resultados.append(usuario)
    return resultados

# Valida los departamentos a los que pertenece cada usuario. Tiene como entrada
# la lista de usuarios y devuelve un vector con los departamnetos a los que 
# que pertenece cada usuario, en el mismo orden que los usuarios
def asigna_departamento(user_list):
    with open("departamentos.txt") as file:
        db = [line.strip().split() for line in file]
    
    result = []
    for user in user_list:
        department = None
        for entry in db:
            if user == entry[1]:
                department = entry[0]
                break
        result.append(department)
    return result

# Valida las VLANs a los que pertenece cada departamento. Tiene como entrada
# la lista de departamentos y devuelve un vector con las VLANs a las que 
# que pertenece cada departamento, en el mismo orden que los departamentos
def asigna_vlan(dep_list):
    with open("grupo_vlan.txt") as file:
        db = [line.strip().split() for line in file]
    
    result = []
    for dep in dep_list:
        vlan = None
        for entry in db:
            if dep == entry[1]:
                vlan = entry[0]
                break
        result.append(vlan)
    return result

# Crea la matriz NAC con toda la informacion validada
def crea_matriz(nodos,puertos,macs,user_per_mac,dep_per_user,vlan_per_dep):
    matriz=[]
    for i in range(len(nodos)):
        matriz.append([nodos[i] , puertos[i], macs[i], user_per_mac[i], 
                       dep_per_user[i], vlan_per_dep[i]])
    print("\n|================================================================|")
    print("|===================== RESUMEN DE TOPOLOGIA =====================|")
    for i in range(len(matriz)):
        print(matriz[i])
    print("|================================================================|\n")
    return matriz

# Asigna las VLANs a los usuarios de la matriz NAC mediante el comando PUT
# y con la publicacion de un archivo tipo JSON con el protocolo 802.1q
def put_vlan(controller_ip, username, password, node_id, port_number1, mac, 
             usuario, departamento, vlan_id):
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
    