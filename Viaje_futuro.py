# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:09:13 2022

@author: danie
"""
#########################
#Definición de funcoines#
#########################
def comprobar_dato(hora):
    
    """
    La función comprobar, comprueba si la cadena ingresada por el usuario 
    contiene sólo logitos. En este caso permite que el usuario agregue números
    enteros debido a que el comando "isdigit()" no toma al punto (.) como parte
    de los digitos. 
    """
    if hora.isdigit() == False:
        print("formato invalido")
        quit()
    else:
        pass
    
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
    
########################################
#variables str para la entrada de datos#
########################################

hora_pedida = "Inserte un número entero de horas entre la 1 y las 12: "
minuto_pedido = "su hora actual es {} horas con ¿cúantos minutos?, inserte un\
 número entero de minutos entre 00 y 59: "
am_pm = "¿La hora ingresada es am o pm? "
hora_usu_final = "Su hora actual es {}:{} {}"
viaje_futuro = "¿Cuántas horas en el futuro quieres ir? Inserte un número\
 entero de horas: "
minutos_futuro = "Usted quiere viajar {} horas al futuro, con ¿cúantos minutos?\
 inserte un número entero de minutos: "
viaje_futuro_final = "Usted quiere viajar {} horas y {} minutos al futuro"
hora_final = "Dado que viajo {} horas y {} minutos al futuro, la hora actual\
 es {}:{} {}"
formato_inv = "Formato invalido."
am_2 = "Am"
pm_2 = "Pm"

############################
#pedido de datos al usuario#
############################

hora_usu = input(hora_pedida)
comprobar_dato(hora_usu)
hora_usu=int(hora_usu)


if hora_usu <= 0 or hora_usu > 12:
    print(formato_inv)
    quit()    
    
minuto_usu = input(minuto_pedido.format(hora_usu))
comprobar_dato(minuto_usu)
minuto_usu = int(minuto_usu)


if minuto_usu < 0 or minuto_usu > 59:
    print(formato_inv)
    quit()
    
am_1 = ["am","Am","aM","AM"] #se crea una lista para las opciones de am
pm_1 = ["pm","Pm","pM","PM"] #se crea una lista para las opciones de pm

horario = str(input(am_pm))
VerNum=horario.isdigit()
if VerNum == True:
    print(formato_inv)
    quit()
elif horario not in am_1 and horario not in pm_1:
        print(formato_inv)
        quit()
    
print(hora_usu_final.format(hora_usu, minuto_usu,horario))

#Se pide las horas y minutos que el usuario quiere viajar

futuro_usu = input(viaje_futuro)
comprobar_dato(futuro_usu)
minuto_futuro_usu = input(minutos_futuro.format(futuro_usu))
comprobar_dato(minuto_futuro_usu)
futuro_usu =int(futuro_usu)
minuto_futuro_usu =int(minuto_futuro_usu)

print(viaje_futuro_final.format(futuro_usu, minuto_futuro_usu))

##########################
#Procedimiento matematico# 
##########################

minutos_viaje = minuto_futuro_usu%60
minutos_totales = minuto_usu + minuto_futuro_usu
horas_de_minutos = int(minutos_totales/60) #Se hace un conteo de cuantas horas es
                                        #la suma de minutos
minutos_restantes =   minutos_totales%60 #los minutos sobrantes 

suma_de_horas_viaje= futuro_usu + horas_de_minutos
suma_de_horas = hora_usu + futuro_usu + horas_de_minutos #total de horas
hora_futura = suma_de_horas%12 #hora final entre 1 y 12
medidor_am_pm=int(suma_de_horas/12) #De la paridad de este numero depende am y pm                                 
                                        
                                        
#calculador hora futuro am o pm



numero= paridad(medidor_am_pm)

#################
#Salida de datos#
#################


if numero == True:
    print((hora_final).format(suma_de_horas_viaje,minutos_viaje,\
                              hora_futura,minutos_viaje,horario))
elif horario in am_1:
    print((hora_final).format(suma_de_horas_viaje,minutos_restantes,\
                                  hora_futura,minutos_restantes,pm_2))
else:
    print((hora_final).format(suma_de_horas_viaje,minutos_restantes,\
                                  hora_futura,minutos_restantes,am_2))