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

def buscar_usuarios(macs):
    with open("macsDB.txt", "r") as file:
        usuarios_macs = [linea.strip().split() for linea in file]
    resultados = []
    
    for mac in macs:
        for usuario, mac_usuario in usuarios_macs:
            if mac == mac_usuario:
                resultados.append(usuario)
    return resultados


