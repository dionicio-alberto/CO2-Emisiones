import pandas as pd
import matplotlib.pyplot as plt

def zonas():
    print("Has seleccionado zonas geograficas\n")
    print("Tenemos información de las siguentes zonas geograficas")
    zonas_geograficas=['Africa Eastern and Southern','Africa Western and Central','Arab World','Central Europe and the Baltics',
                   'Caribbean small states','East Asia & Pacific','Europe & Central Asia','Euro area','European Union','Latin America & Caribbean',
                   'Middle East & North Africa','North America','OECD members','Pacific island small states','South Asia',
                   'Sub-Saharan Africa','World']
    for i in range(17):
        print(f'{i+1}) {zonas_geograficas[i]}')
        
    print('¿De que zona geografica quieres saber la información? (1-17): ')
    zona=int(input())
    while zona not in range(1,18):
        print('Introduzca un valor valido')
        zona=int(input())
        
    nombre=zonas_geograficas[zona-1]
    return nombre

def paises(data):
    print('Has seleccionado paises\n')
    print('Ingresa el nombre del pais en ingles: ')
    nombre = input('')
    nombre.capitalize()
    esta = nombre in data['country_name'].values
    while esta == False:
        print('El pais no se encuentra o ha sido escrido de forma incorrecta, escribelo nuevamente')
        nombre = input()
        nombre=nombre.capitalize()
        esta = nombre in data['country_name'].values
    return nombre
    

def grafica(nombre,data):
    data2 = data[data['country_name']==nombre]
    data2.plot(x='year',y='value',title=f'Emisiones de CO2 desde 1960 hasta 2019\n{nombre}',
               legend='hola',xlabel='Año',ylabel='Emisiones de CO2 en Kilotones')
    plt.show()
    

def que_ver(data):
    print('''
    Bienvenido a este programa el cual permite como ha evolucionado la emision de CO2 desde 1960 hasta 2019
    en diversos paises y zonas geograficas
    ''')
    print('Primero, desaeas ver el crecimiento por zona geografica o por pais')
    print('''
    1) Por zona geogfrafica
    2) Por país''')
    a = int(input())
    while a != 1 and a != 2:
        print('Ingrese un valor válido')
        a = int(input())
    
    #Caso en que queremos saber la evolucion de una zona geografica
    if a == 1: 
        nombre = zonas()
    
    elif a == 2:
        nombre = paises(data)
    
    grafica(nombre,data)
    