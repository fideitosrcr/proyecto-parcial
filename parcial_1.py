# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 21:08:32 2022

@author: josad
"""

#Se difine una función que compruebe la paridad de un número especifico
def paridad(numero):
    """
    La función paridad requiere un número entero o decimal, a este número
    se le aplicara el operador modulo entre 2 y si su residuo es cero,
    propidad de los números pares, retornara True, en caso contrario 
    retornara False.
  
    """
    if numero % 2 == 0:
        return(True)
    else:
        return(False)
    
#variables str para la entrada de datos
    
hora_pedida = "Inserte una hora entre la 1 y las 12: "
am_pm = "¿La hora ingresada es am o pm? "
viaje_futuro = "¿Cuántas horas en el futuro quieres ir? "
formato_inv = "Formato invalido."

#pedido de datos al usuario

hora_usu = input(hora_pedida)
if hora_usu.isdigit() == False:
    print(formato_inv)
    quit()
hora_usu = int(hora_usu)
if hora_usu!=int(hora_usu):
    print(formato_inv)
    quit()
if hora_usu <= 0 or hora_usu > 12:
    print(formato_inv)
    quit()    
    
am_1 = ["am","Am","aM","AM"] #se crea una lista para las opciones de am
pm_1 = ["pm","Pm","pM","PM"] #se crea una lista para las opciones de pm

horario = str(input(am_pm))
VerNum=horario.isdigit()
if VerNum == True or horario not in am_1 or horario not in pm_1:
    print(formato_inv)
    quit()
futuro_usu = int(input(viaje_futuro))

#Procedimiento matematico 

suma_de_horas = hora_usu + futuro_usu
hora_futura = suma_de_horas%12
medidor_am_pm=int(suma_de_horas/12)

#calculador hora futuro am o pm



am_2 = "Am"
pm_2 = "Pm"

numero= paridad(medidor_am_pm)

if numero == True:
    print(("Dado que viajo {} al futuro, la hora actual es {} {}")
          .format(futuro_usu,hora_futura,horario))
else:
    if horario in am_1:
        print(("Dado que viajo {} al futuro, la hora actual es {} {}")
              .format(futuro_usu,hora_futura,pm_2))
    else:
        print(("Dado que viajo {} al futuro, la hora actual es {} {}")
              .format(futuro_usu,hora_futura,am_2))
    
    
    
    
 #pruf   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    