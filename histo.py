# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 16:02:42 2022

@author: josad
"""
import matplotlib.pyplot as plt

conversor = lambda x:x/2.54 #convierte los centimetros en pulgadas

class Histograma:
    """
    Esta clase recoge datos los cuales serán luego graficados en un histograma
    """
    def __init__(self,v1, v2, v3, v4, v5, v6, v7, v8,\
                 v9, v10):
        self.D1=v1
        self.D2=v2
        self.D3=v3
        self.D4=v4
        self.D5=v5
        self.D6=v6
        self.D7=v7
        self.D8=v8
        self.D9=v9
        self.D10=v10
        
    def lista(self):
        """
        Se define un metodo lista el cual crea una lista con los datos ingresados
        en la clase Histograma
        """
        datos=[self.D1,self.D2,self.D3,self.D4,self.D5,self.D6,self.D7,self.D8\
               ,self.D9,self.D10]
            
        return(datos)
    
    
    def graficar(self):
        """
        El método graficar utiliza la lista creada con el método "lista" y la 
        grafica como un histograma. También decora la grafica con titulo, 
        titulo en los ejer, color de relleno, color de bordes, un leguen y la 
        en formato PDF.
        """
        fig_1 = plt.figure(figsize=(conversor(8),conversor(13)),constrained_layout=True)
        ax1=fig_1.add_subplot()
        n= self.lista()
        histo = ax1.hist(n, bins=10,edgecolor='pink',facecolor='skyblue',\
                         label="Barra de datos", )
        deco=(plt.legend(),plt.title("Histograma de datos añadidos"),\
                 plt.xlabel("Datos"),plt.ylabel("Frecuencia de los datos"),
                 plt.minorticks_on())
        
        gra = plt.show()
        save= plt.savefig('Figura.pdf', format='pdf')
        
        return(histo,gra,deco,save)


"""
Para impletar la clase "Histograma" se hace un estudio de la cantidad de lluvias
en 10 meses, para así saber cual puede ser la cantidad de veces que llovera en  
noviembre.
Los datos son de enero a octubre respectivamente 
10, 15, 14, 10, 12, 10, 11, 12, 14, 15

"""

lo=Histograma(10, 15, 14, 10, 12, 10, 11, 12, 14, 15)


lo.graficar()

        
        
#pruf