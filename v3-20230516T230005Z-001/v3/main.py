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
import topologia
import helpers
import time

ip_controlador = '192.168.18.21'    # Direccion IP del controlador ODL
username = 'admin'                  # Nombre de usuario del controlador ODL
password = 'admin'                  # Contraseña del controlador ODL
matriz_aux = []                     # Matriz NAC

while True:
    #==========================================================================
    #========================================================================== 
    #recolecta la informacion actual de la topologia
    puertos,nodos,mac = topologia.muestra_topo(ip_controlador,username,password)
    
    # ordena las macs detectadas de la topologia en una matriz
    macs = helpers.ordena_macs(mac)  
    
    # compara macs de hosts contectados con la DB y los relaciona con su user
    user_per_mac = helpers.buscar_usuarios(macs) 
    
    # compara users detectados con la DB y los relaciona con su departamento
    dep_per_user = helpers.asigna_departamento(user_per_mac)
    
    # compara departamentos de users con la DB y los relaciona con su VLAN
    vlan_per_dep = helpers.asigna_vlan(dep_per_user)
    
    # crea una matriz con toda la informacion recolectada de la topologia y DB
    matriz = helpers.crea_matriz(nodos, puertos, macs,user_per_mac, 
                                 dep_per_user, vlan_per_dep)
    
    # compara cambios en la topologia creada
    if matriz_aux != matriz:
        # asigna VLANs dinamicamente con la informacion de la matriz 
        
        for i in range(len(matriz)):
             helpers.put_vlan(ip_controlador, username, password, matriz[i][0], 
                                  matriz[i][1], matriz[i][2], matriz[i][3],
                                  matriz[i][4], matriz[i][5])
    else:
        print("NO EXISTEN CAMBIOS EN LA TOPOLOGIA")
    
    matriz_aux = matriz
    #==========================================================================
    #==========================================================================
    time.sleep(20)
