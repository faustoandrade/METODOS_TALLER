import random
import csv

def crearLista():
	lista = list()
	return lista

def imprimirLista(lista):
	print lista

def llenarLista(lista, limite):
	for i in range(0, limite):
		lista.append(random.randint(-9999, 9999))

def llenar(limite):
	lista=[]
	for i in range(0, limite):
		lista.append(random.randint(1000, 9999))
	return lista

def nombreArchivo():
	nombre = raw_input("Ingrese nombre del archivo: ")
	return nombre

def crearCsv(lista, nombre):
	datos = open(nombre + ".csv", "w")
	datos_csv = csv.writer(datos)
	datos_csv.writerow(lista)
	datos.close()

def leerCsv(lista_2, nombre):
	datos = open(nombre + ".csv", "r")
	datos_csv = csv.reader(datos, delimiter = ",")
	for variable in (datos_csv):
		lista_2.append(variable)
	datos.close()
	return lista_2

def longitud(lista):
	return len(lista)

def imprimirTiempo(tiempo_final):
	print ("Proceso finalizado en %0.5f segundos" %tiempo_final)

def arreglalista(lista,nlista):
	for i in lista [0]:
		nlista.append(int(i))
	return nlista