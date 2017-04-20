from funciones import *
from metodosOrd import *
import json
import threading
import time

def main():
	mnu = ['                 METODOS DE ORDENAMIENTO\n''1.INSERCION', '2.MEZCLA', '3.HEAP SORT', '4.QUICKSORT', '5.COUNTING SORT',
			 '6.RADIX SORT', '11.Salir']

	for i in mnu:
		print i
	opcion = int(input("Selecione La operacion que Desea Realizar "))
	if opcion == 1:
		valor = int(input("Ingrese la cantidad de Datos a Ordenar"))
		tiempo_inicial = time.time()
		lista = crearLista()
		nombre = nombreArchivo()
		llenarLista(lista, valor)
		crearCsv(lista, nombre)
		print "           Insercion Directa        "
		imprimirLista(lista)

		# ordenar
		lista_ordenada = crearLista()
		leerCsv(lista_ordenada, nombre)
		nlista = crearLista()
		nlista2 = arreglalista(lista_ordenada, nlista)
		tam = longitud(nlista2)
		insercionDirecta(nlista2, tam)
		tiempo_inicial_hilo = time.time()
		hilo2 = threading.Thread(target=insercionDirecta, args=(lista, tam))
		hilo2.start()
		print "Lista Ordenada"
		imprimirLista(nlista2)
		nombre_final = nombreArchivo()
		crearCsv(lista_ordenada, nombre_final)
		print "Tiempo Demora Sin Hilos"
		tiempo_final = time.time() - tiempo_inicial
		imprimirTiempo(tiempo_final)
		print "Tiempo Demora Con Hilos"
		tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
		imprimirTiempo(tiempo_final_Hilos)

	if opcion == 2:
		valor = int(input("Ingrese la cantidad de Datos a Ordenar"))
		tiempo_inicial = time.time()
		lista = crearLista()
		nombre = nombreArchivo()
		llenarLista(lista, valor)
		crearCsv(lista, nombre)
		print "           Mezcla        "
		imprimirLista(lista)

		# ordenar
		lista_ordenada = crearLista()
		leerCsv(lista_ordenada, nombre)
		nlista = crearLista()
		nlista2 = arreglalista(lista_ordenada, nlista)
		tam = longitud(nlista2)
		mergeSort(nlista2)
		tiempo_inicial_hilo = time.time()
		hilo2 = threading.Thread(target=mergeSort, args=(nlista2))
		hilo2.start()
		print "Lista Ordenada"
		imprimirLista(nlista2)
		nombre_final = nombreArchivo()
		crearCsv(lista_ordenada, nombre_final)
		print "Tiempo Demora Sin Hilos"
		tiempo_final = time.time() - tiempo_inicial
		imprimirTiempo(tiempo_final)
		print "Tiempo Demora Con Hilos"
		tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
		imprimirTiempo(tiempo_final_Hilos)

	if opcion == 3:
		valor = int(input("Ingrese la cantidad de Datos a Ordenar"))
		tiempo_inicial = time.time()
		lista = crearLista()
		nombre = nombreArchivo()
		llenarLista(lista, valor)
		crearCsv(lista, nombre)
		print "              METODO HEAPSORT         "
		imprimirLista(lista)

		# ordenar
		lista_ordenada = crearLista()
		leerCsv(lista_ordenada, nombre)
		nlista = crearLista()
		nlista2 = arreglalista(lista_ordenada, nlista)
		#tam = longitud(nlista2)
		heapsort(nlista2)
		tiempo_inicial_hilo = time.time()
		hilo3 = threading.Thread(target=heapsort, args=(nlista2))
		hilo3.start()
		print "Lista Ordenada"
		imprimirLista(nlista2)
		nombre_final = nombreArchivo()
		crearCsv(lista_ordenada, nombre_final)
		print "Tiempo Sin Hilos"
		tiempo_final = time.time() - tiempo_inicial
		imprimirTiempo(tiempo_final)
		print "Tiempo Con Hilos"
		tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
		imprimirTiempo(tiempo_final_Hilos)

	if opcion == 4:
		valor = int(input("Ingrese la cantidad de Datos a Ordenar"))
		tiempo_inicial = time.time()
		lista = crearLista()
		nombre = nombreArchivo()
		llenarLista(lista, valor)
		crearCsv(lista, nombre)
		print "              METODO QUICKSORT          "
		imprimirLista(lista)

		# ordenar
		lista_ordenada = crearLista()
		leerCsv(lista_ordenada, nombre)
		nlista = crearLista()
		nlista2 = arreglalista(lista_ordenada, nlista)
		tam = longitud(nlista2)
		quicksort(nlista2, 0, tam - 1)
		tiempo_inicial_hilo = time.time()
		hilo1 = threading.Thread(target=quicksort, args=(nlista2, 0, tam - 1))
		hilo1.start()
		print "Lista Ordenada"
		imprimirLista(nlista2)
		nombre_final = nombreArchivo()
		crearCsv(lista_ordenada, nombre_final)
		print "Tiempo Sin Hilos"
		tiempo_final = time.time() - tiempo_inicial
		imprimirTiempo(tiempo_final)
		print "Tiempo Con Hilos"
		tiempo_final_Hilos = time.time - tiempo_inicial_hilo
		imprimirTiempo(tiempo_final_Hilos)

	if opcion == 5:
		valor = int(input("Ingrese la cantidad de Datos a Ordenar"))
		tiempo_inicial = time.time()
		lista = crearLista()
		nombre = nombreArchivo()
		llenarLista(lista, valor)
		crearCsv(lista, nombre)
		maximo = max(lista)
		print "              METODO COUNTING SORT         "
		#imprimirLista(lista)

		# ordenar
		lista_ordenada = crearLista()
		leerCsv(lista_ordenada, nombre)
		nlista = crearLista()
		nlista2 = arreglalista(lista_ordenada, nlista)
		tam = longitud(nlista2)
		count_sort(nlista2, maximo)
		tiempo_inicial_hilo = time.time()
		hilo1 = threading.Thread(target=count_sort, args=(nlista2, maximo))
		hilo1.start()
		print "Lista Ordenada"
		#imprimirLista(nlista2)
		nombre_final = nombreArchivo()
		crearCsv(lista_ordenada, nombre_final)
		print "Tiempo Sin Hilos"
		tiempo_final = time.time() - tiempo_inicial
		imprimirTiempo(tiempo_final)
		print "Tiempo Con Hilos"
		tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
		imprimirTiempo(tiempo_final_Hilos)

	if opcion == 6:
		valor = int(input("Ingrese la cantidad de Datos a Ordenar"))
		tiempo_inicial = time.time()
		lista = llenar(valor)
		nombre = nombreArchivo()
		#llenarLista(lista, valor)
		crearCsv(lista, nombre)
		print "              METODO RADIX SORT     "
		#imprimirLista(lista)


		# ordenar
		#lista_ordenada = crearLista()
		#leerCsv(lista_ordenada, nombre)
		#nlista = crearLista()
		#nlista2 = arreglalista(lista_ordenada, nlista)
		#tam = longitud(nlista2)
		lista_ordenada=radix_sort(lista)
		tiempo_inicial_hilo = time.time()
		hilo1 = threading.Thread(target=radix_sort, args=(lista))
		hilo1.start()
		print "Lista Ordenada"
		#imprimirLista(lista_ordenada)
		nombre_final = nombreArchivo()
		crearCsv(lista_ordenada, nombre_final)
		print "Tiempo Sin Hilos"
		tiempo_final = time.time() - tiempo_inicial
		imprimirTiempo(tiempo_final)
		print "Tiempo Con Hilos"
		tiempo_final_Hilos = time.time - tiempo_inicial_hilo
		imprimirTiempo(tiempo_final_Hilos)


	if opcion < 8:
		raw_input("\n PRESIONE ENTER PARA VOLVER AL MENU:")

if __name__ == '__main__':
		main()