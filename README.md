<h1 align="center"> Viaje al futuro y lluvias en noviembre </h1>

 

![Z7udqT3-1024x350](https://user-images.githubusercontent.com/104390248/193504835-992d5f77-7596-49a1-b6a7-aa9962e8b5fd.jpeg)

## Índice

* [Título e imagen de portada](#Título-e-imagen-de-portada)

* [Índice](#índice)

* [Características de la aplicación y demostración](#Características-de-la-aplicación-y-demostración)

* [Conclusión](#conclusión)

## Características de la aplicación y demsotración

El proyecto consta de dos partes, cada una de estas no tienen algun tipo de relación entre sí, sólo se añaden para la utilización y ejemplificación al lector.

En primer lugar se realiza el proyecto `viaje al futuro` el cual cuenta con un programa que interactua con el usuario pidiendole de manera clara los datos que debe ingresar para que el programa corra correctamente. El programa `viaje al futuro` te pediera una hora entre la 1 y las 12, luego te pedira los minutos que acompañan la hora, también te pide que ingreses si esa hora es am o pm, por ultimo el programa te pregutara cuantas horas y minutos quieres viajar al futuro; al ingresar las horas y los minutos te dira la hora am o pm es después de haber realizado tu viaje. A continuación un ejemplo del programa.


![viaje](https://user-images.githubusercontent.com/104390248/193508547-714c82f6-8c02-4718-b372-a6a76cc958b2.PNG)


El programa `viaje al futuro` cuenta con dos funciones internas una es `paridad` que perimite comprobar si el número de horas final del viaje es par o impar, dado que sabiendo si es par o impar se puede saber si es am o pm. También cuenta con una función `comprobar` esta tiene internamente el comando `isdigit`, la función `comprobar`revisa los datos ingresados y en caso de que los datos no sean los que se están pidiendo imprime `formato invalido` y cierra el codigo. A continuación un ejemplo.

![salir](https://user-images.githubusercontent.com/104390248/193509201-f5cbc3d0-2398-4683-98a7-8750e82ae425.PNG)

En segundo lugar se tiene la clase `Histograma`, esta clase pide `10` valores para luego graficarlos en un histograma utilizado la libreria `Matplotlib`.
La clase`Histograma` contiene 3 métodos el primero es un método `__init__` que se encarga de recoger los datos ingresados a la clase`Histograma`
el segundo es el método `lista` este se encarga de crear una lista con los datos que se ingresan enla clase. Por ultimo, el método `graficar` este metodose encarga de graficar el histograma y decorar la grafica con colores, titulo principal, titulos en los ejes, las dimensiones del lienzo y la ocupación de la grafica, entre otros.

La clase `Histograma` puede servir para la predicción de datos a futuro, por ejemplo, se utilizó con un ejemplo de las lluvias de los 10 primeros meses del año, es decir el número de veces que llovio en cada mes y con estos datos (de manera burda) predecir las veces que puede llover en noviembre. 

Los datos son

|meses                    | veces que llovio      |
|-------------------------|-----------------------|
| enero                   |  10                   |
| febrero                 |  15                   |
| marzo                   |  14                   |
| abril                   |  10                   |
| mayo                    |  12                   |
| junio                   |  10                   |
| julio                   |  11                   |
| agosto                  |  12                   |
| septiembre              |  14                   |
| octubre                 |  15                   |

Al ingresarlos a la clase y graficarlo, el histograma de datos es el siguiente.

![histo](https://user-images.githubusercontent.com/104390248/193511431-4c953139-d9f0-4c53-bac7-59287aa42cc6.png)

## Conclusión 

La realización de los programas que se encuentran en este repositorio han sido de gran ayuda para expandir mi conocimiento en el manejo de `condicionales, clases, metodos y funciones` los programas están totalmente abiertos a consejos y usos. Como conclusión el programa `viaje al futuro` se basa en la utilización de condicionales y la clase `Histograma` se basa en la libreria `matplotlib`, la manipulación de los objetos de una clase y un cominezo a ver ciencia de datos.
