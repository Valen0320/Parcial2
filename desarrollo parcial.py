# Importacion de librerias
import matplotlib.pyplot as plt
import pandas as pd

# Leer archivo excel 
archivo_excel = pd.read_excel('Futbol_Partidos.xlsx')

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	print ("Selecciona una opción")
	print ("\n\t1 - Cantidad de goles de los equipos locales y grafica \n\n\t2 - Cantidad de goles de los equipos visitantes y grafica")
	print ("\n\t3 - Cantidad total de goles de todos los partidos y grafica \n\n\t4 - Cantidad de goles de los equipos locales por campeonato y grafica")
	print ("\n\t5 - Cantidad de goles de los equipos visitantes por campeonato y grafica \n\n\t6 - Cantidad total de goles por campeonato y grafica")
	print ("\n\t7 - Gráfico de barras de cantidad de partidos por selección \n\n\t8 - Gráfico de barras apiladas horizontales de cantidad de partidos local y visitante por selección")
	print ("\n\t9 - Selección que más goles realizó y selección que mas goles recibió en todos los campeonatos")
    
	# Mostramos el menu
menu()

    # solicitamos una opción al usuario
opcionMenu = input("inserta un numero valor >> ")


# Funcion para hacer las graficas
def graficar(xlabel, ylabel, title, groupby, count, graph, colors = ['BLUE','MAGENTA']):
    # Generar el grafico
    fig, ax = plt.subplots()
    ax.set_title(title)

# Crear el grafico
    archivo_excel.groupby(groupby, sort = True)[count].count().plot(kind = graph, color = colors)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

# Funciones que resuelven las preguntas
def cantidad_goles_locales(): # Ejercicio 1
    equipo_local = archivo_excel['goles_local'].sum()
    print("Los goles totales de los equipos locales son: ", equipo_local)
    graficar('cantidad de gooles', 'equipos', 'goles locales', 'local', 'goles_local', 'barh')
    

    
def cantidad_goles_visitantes(): # Ejercicio 2
    equipo_visitante = archivo_excel['goles_visita'].sum()
    print("Los goles totales de los equuipos visitantes son: ", equipo_visitante)
    graficar('cantidad de goles', 'equipos', 'goles visitantes', 'visitante', 'goles_visita', 'barh')
    


def cantidad_goles_totales(): # Ejercicio 3
    total_goles = archivo_excel['goles_local'].sum() + archivo_excel['goles_visita'].sum()     
    print("La suma total de los goles de los equipos locales y visitantes es: ", total_goles)
    
    equipo_local = archivo_excel.groupby("local", sort=True)["goles_local"].count()
    equipo_visitante = archivo_excel.groupby("visitante", sort=True)["goles_visita"].count()
    equipos = sorted(archivo_excel['local'].unique())

    total = []
    for a, b in zip(equipo_local, equipo_visitante):
        total.append(a+b)
	
    # Generar el grafico    
    fig, ax = plt.subplots()
    ax.set_title('Total goles de todos los partidos')
    ax.set_ylabel('Equipos')
    ax.set_xlabel('Total de goles')

    plt.barh(equipos,total)
    plt.show()
    


def goles_local_por_campeonato(): # Ejercicio 4
    goles_local_por_campeonato = archivo_excel.groupby('torneo')['goles_local'].sum()
    print("Los goles totales por campeonato de los locales son:\n" , goles_local_por_campeonato)  
    graficar('goles locales', 'equipos', 'goles por campeonato local', 'torneo', 'goles_local', 'barh')
    


def goles_visitante_por_campeonato(): # Ejercicio 5
    goles_visita_por_campeonato = archivo_excel.groupby('torneo')['goles_visita'].sum()
    print("Los goles totales por campeonato de los visitantes son:\n" , goles_visita_por_campeonato)  
    graficar('goles visitantes', 'equipos', 'goles por campeonato visita', 'torneo', 'goles_visita', 'barh')
    


def goles_totales_por_campeonato(): # Ejercicio 6
    total_goles_por_campeonato = archivo_excel.groupby('torneo')['goles_local'].sum() + archivo_excel.groupby('torneo')['goles_visita'].sum()
    print("La cantidad de goles por torneo es: ", total_goles_por_campeonato)
    
    
    total_torneo_local = archivo_excel.groupby("torneo", sort=True)["goles_local"].count()
    total_torneo_visitante = archivo_excel.groupby("torneo", sort=True)["goles_visita"].count()
    equipos = sorted(archivo_excel['torneo'].unique())

    total = []
    for a, b in zip(total_torneo_local, total_torneo_visitante):
        total.append(a+b)
	
    # generar el grafico
    fig, ax = plt.subplots()
    ax.set_title('goles totales por campeonato')
    ax.set_xlabel('goles totales')
    ax.set_ylabel('torneos')

    plt.barh(equipos,total)
    plt.show()
    

 
def partidos_por_seleccion(): # Ejercicio 7
    total_partidos = archivo_excel.groupby('local', sort=True)['gana_local'].count()
    print("La cantidad de partidos por equipo en total es:" , total_partidos)
    graficar('cantidad partidos', 'selecciones', 'partidos totales por seleccion', 'local', 'gana_local', 'barh')
             


def partidos_local_y_visitante(): # Ejercicio 8
	locales = archivo_excel[['local', 'gana_local']]
	visitantes = archivo_excel[['visitante', 'gana_visita']]
	equipos = sorted(archivo_excel['local'].unique())
    
    # Declaracion de variables
	gano = 0
	perdio = 0
	equipos_resultados = []
	resultados = []

    # Proceso 
	for equipo in equipos:
		for index, row in locales.iterrows():
			if row.local == equipo:
				if row.gana_local == 1:
					gano+= 1
				else:
					perdio+=1
		resultados.append(equipo + 'G')
		resultados.append(equipo + 'P')
		equipos_resultados.append(gano)
		equipos_resultados.append(perdio)

    # Generar el grafico
	fig, ax = plt.subplots()
	ax.set_title('Total de todos los resultados')
	ax.set_ylabel('Equipos')
	ax.set_xlabel('Margen de victoria y derrota por equipo')

	plt.barh(resultados,equipos_resultados)
	plt.show()
    


def test(x): # Ejercicios 9 y 10
    return x[1]

def selecciones_que_mas_goles_hiciereon_y_recibieron():
    datos_local = archivo_excel[['local', 'goles_local', 'visitante', 'goles_visita']]
    equipos = sorted(archivo_excel['local'].unique())
    
    # Declaracion de variables
    metio = 100
    metieron = 120
    equipos_resultados = []
    resultados_metidos = []
    resultados_metieron = []
    
    # Proceso
    for equipo in equipos:
        for index, row in datos_local.iterrows():
            if row.local == equipo:
                metio+= row.goles_local
                metieron+= row.goles_visita
        resultados_metidos.append([equipo, metio])
        resultados_metieron.append([equipo, metieron])
        
        metio = 0
        metieron = 0
        
    print("El equipo que mas goles metio fue: ", sorted(resultados_metidos, key = test, reverse=True)[0])
    print("El equipo que mas goles recibio fue: ", sorted(resultados_metieron, key = test, reverse=True)[0])


if opcionMenu==1:
	print (cantidad_goles_locales())
	input("Has pulsado la opción 1...\npulsa una tecla para continuar")
elif opcionMenu=="2":
	print (cantidad_goles_visitantes())
	input("Has pulsado la opción 2...\npulsa una tecla para continuar")
elif opcionMenu=="3":
	print (cantidad_goles_totales())
	input("Has pulsado la opción 3...\npulsa una tecla para continuar")
elif opcionMenu=="4":
	print (goles_local_por_campeonato())
	input("Has pulsado la opción 4...\npulsa una tecla para continuar")
elif opcionMenu=="5":
	print (goles_visitante_por_campeonato())
	input("Has pulsado la opción 5...\npulsa una tecla para continuar")
elif opcionMenu=="6":
	print (goles_totales_por_campeonato())
	input("Has pulsado la opción 6...\npulsa una tecla para continuar")
elif opcionMenu=="7":
	print (partidos_por_seleccion())
	input("Has pulsado la opción 7...\npulsa una tecla para continuar")
elif opcionMenu=="8":
	print (partidos_local_y_visitante())
	input("Has pulsado la opción 8...\npulsa una tecla para continuar")
elif opcionMenu=="9":
	print (selecciones_que_mas_goles_hiciereon_y_recibieron())
	input("Has pulsado la opción 9...\npulsa una tecla para continuar")
else:
    print("Introduce una opción correcta")
