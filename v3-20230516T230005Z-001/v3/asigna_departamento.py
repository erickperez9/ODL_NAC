# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 23:35:53 2023

@author: Mateo
"""

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

