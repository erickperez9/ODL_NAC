# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:26:18 2023

@author: Mateo
"""

import requests
import re
from requests.auth import HTTPBasicAuth

def es_switch(palabra):
    return bool(re.match("^o", palabra))

def es_host(host_name):
    return bool(re.match("^h", host_name))

def muestra_topo(controller_ip,username,password):
    url = f'http://{controller_ip}:8181/restconf/operational/network-topology:network-topology/topology/flow:1/'
    
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    puertos=[]
    nodos=[]
    puertos1=[]
    nodos1=[]
    host1=[]
    data = response.json()
    ban=1
    for sw in data['topology'][0]['link']:
        source_nodeSW = sw['source']['source-node']
        source_tpSW = sw['source']['source-tp']
        dest_nodeSW = sw['destination']['dest-node']
        dest_tpSW = sw['destination']['dest-tp']
        
        if ban==1:
            print("\n|================================================================|")
            print("|========================== TOPOLOGIA SW ========================|")
            print("|================================================================|")
            print("| Nodo Org  |  Puerto Org | Conectado a| Nodo Dst |  Puerto Dst  |")
            print("|----------------------------------------------------------------|")
        if es_switch(source_nodeSW) and es_switch(source_tpSW) and es_switch(dest_tpSW) and es_switch(dest_nodeSW):
            puertos.append(source_tpSW)
            nodos.append(source_nodeSW)
            print(f'|{source_nodeSW} | {source_tpSW} | {dest_nodeSW} | {dest_tpSW} |')
        ban=ban+1
    print("|================================================================|\n")       
    ban=1      
    
    for host in data['topology'][0]['link']:
        source_node = host['source']['source-node']
        source_tpHost = host['source']['source-tp']
        dest_nodeHost = host['destination']['dest-node']
        dest_tpHost = host['destination']['dest-tp']
        
        if ban==1:
            print("\n|=============================================================|")
            print("|====================== TOPOLOGIA HOSTS ======================|")
            print("|=============================================================|")
            print("| Nodo Org  |  Puerto Org | Conectado a  |         Hosts      |")
            print("|-------------------------------------------------------------|")      
        if es_switch(source_node) and es_switch(source_tpHost) and es_host(dest_nodeHost) and es_host(dest_tpHost):
            source_node=host['source']['source-node']
            source_tpHost = host['source']['source-tp']
            dest_nodeHost = host['destination']['dest-node']
            dest_tpHost = host['destination']['dest-tp']
            print(f'|{source_node} | {source_tpHost} | {dest_nodeHost} |')
            nodos1.append(source_node)
            puertos1.append(source_tpHost)
            host1.append(dest_nodeHost)
            
            
        ban=ban+1
    print("|=============================================================|\n")
    #return puertos,nodos
    return puertos1, nodos1, host1
        





