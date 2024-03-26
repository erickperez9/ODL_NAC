# -*- coding: utf-8 -*-
"""
Autores: [Erick Pérez P. - Mateo Molina Y.]
Fecha: [14/06/2023]
Descripcion: [El presente codigo ha sido desarrollado y compilado con la 
              version 3.8 de python. El codigo tiene como objetivo la 
              implementacion de un servidor de acceso a la red, NAC, a través 
              de consultas GET al controlador OpenDaylight y a partir de los 
              resultados obtenidos trabajar con archivos tipo JSON. Se hace uso
              funciones de ayuda que realizan los procesos de obtencion del
              estado de la topologia y valicacion de usuarios basados en 
              archivos de texto con informacion de direcciones MAC, usuarios,
              departamentos y VLANs.]

Licencia: [Este código es de libre distribucion para fines academicos e 
           investigativos.]

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

