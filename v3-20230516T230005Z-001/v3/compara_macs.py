# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 23:10:11 2023

@author: Mateo
"""

def buscar_usuarios(macs):
    with open("macsDB.txt", "r") as file:
        usuarios_macs = [linea.strip().split() for linea in file]
    resultados = []
    
    for mac in macs:
        for usuario, mac_usuario in usuarios_macs:
            if mac == mac_usuario:
                resultados.append(usuario)
    return resultados


