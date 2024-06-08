import os
import csv
import json 
from typing import Callable
from random import randint


def validar_lista(lista:list):
    '''
        Recibe una lista, en caso de no ser tipo list da un TypeError
    '''

    if not isinstance(lista,list):
        raise TypeError("Se esperaba una lista")
    

def validar_diccionario(diccionario:dict):
    '''
        Recibe una diccionario, en caso de no ser tipo dict da un TypeError
    '''

    if not isinstance(diccionario,dict):
        raise TypeError("Se esperaba una diccionario")


def get_path_actual(nombre_archivo:str):
    '''
        Se encarga de ubicar el archivo segun el nombre_archivo
    '''
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_csv(nombre_archivo):
    '''
        Se encarga de cargar un archivo csv
        Retorna una lista de diccionarios
    '''
    with open(get_path_actual(f"{nombre_archivo}.csv")) as archivo:
        lista_diccionarios = []
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            lista_diccionarios.append(fila)

    print("El archivo se ha cargado con éxito.")
    return lista_diccionarios

def guardar_csv(nombre_archivo:str,influencers:list):
    """
        Guardo el archivo csv
        En caso de existir te borra lo sobreescribe lo anterior
    """
    nueva_ruta = get_path_actual(f"{nombre_archivo}.csv")

    with open(nueva_ruta, 'w', newline='', encoding = "utf-8") as archivo_modificado:
        escritor_csv = csv.writer(archivo_modificado)
        escritor_csv.writerow(["id","user","likes","dislikes","followers"])
        
        for influencer in influencers:
            escritor_csv.writerow([influencer["id"], influencer["user"], influencer["likes"], influencer["dislikes"], influencer["followers"]])

        print(f"Archivo modificado guardado en: {nueva_ruta}")

def guardar_json(nombre_archivo:str,influencers:list):

    nueva_ruta = get_path_actual(f"{nombre_archivo}.json")
    with open(nueva_ruta, "w", encoding = "utf-8") as archivo:
        json.dump(influencers,archivo,indent=4)
        print(f"Archivo modificado guardado en: {nueva_ruta}")

def mostrar_influencers(influencers:list):
    '''
        Valida la lista
        Recibe una lista
        Imprime en terminal la lista
        Caso contrario da un mensaje de error
    '''
    validar_lista(influencers)
    if(len(influencers) > 0):
        print("                  ****Lista de influencers****")
        print("Id               User            Likes     Dislikes    Followers")
        print("----------------------------------------------------------------")
        for influencer in influencers:
            mostrar_influencer(influencer) 
            print()
    else:
        print('ERROR: La lista no puede ser recorrida')

def mostrar_influencer(influencer:dict):
    '''
        Valida el diccionario
        Recibe un diccionario 
        Imprime en terminal cada elemento
    '''
    validar_diccionario(influencer)
    print(f"{influencer["id"]:<4} {influencer["user"]:>20} {influencer["likes"]:>10} {influencer["dislikes"]:>10} {influencer["followers"]:>10}", end = " ")


def mapear_lista(funct:Callable,lista:list)->list:
    '''
        Recibe una lista,funcion
        Mapea la lista segun la criterio que se envie en funct
        Retorna la lista mapeada
        Caso contrario devuelve una lista vacia
    '''

    validar_lista(lista)
    lista_nueva = []

    if(len(lista) > 0):
        for elem in lista:
            lista_nueva.append(funct(elem))

    return lista_nueva

def filtrar_lista(funct:Callable,lista:list)->list:
    '''
        Recibe una lista,funcion
        Filtra la lista segun la criterio que se envie en funct
        Caso contrario devuelve una lista vacia
    '''

    validar_lista(lista)
    lista_filtrada = []

    if(len(lista) > 0):
        for elem in lista:
            if funct(elem):
                lista_filtrada.append(elem)

    return lista_filtrada

def asignar_estadisticas_aleatorios(influencer:dict)->dict:
    '''
        Recibe un influencer
        Se encarga de manera aleatoria asignarle valores
    '''
    influencer["likes"] = randint(500, 3000)
    influencer["dislikes"] = randint(300, 3500)
    influencer["followers"] = randint(10000, 20000)

    return influencer

def filtrar_clave(clave:str,lista:list)->list:
    '''
        Valida que sea lista y longitud
        Recibe una lista,clave
        Filtra la lista y se queda con el valor de la clave
        Caso contrario devuelve una lista vacia
    '''
    validar_lista(lista)
    lista_filtrada = []
    if(len(lista) > 0):
        for elem in lista:
            lista_filtrada.append(elem[clave])
    return lista_filtrada

def sumar_lista(lista:list)->float:
    '''
        Valida que sea una lista
        Recibe una lista suma sus elementos
        Retorna la suma
    '''  
    validar_lista(lista)
    suma = 0

    if(len(lista) > 0):
        for elem in lista:
            suma += float(elem)
    return suma

def promedio_lista(lista:list)->float:
    '''
        Valida que sea una lista
        Recibe una lista suma sus elementos y saca el promedio
        Retorna el promedio
    '''  
    validar_lista(lista)
    if(len(lista) > 0):
        return sumar_lista(lista) / len(lista)
    
def orden_lista(funct:Callable,lista:list)->None:
    '''
        Valida que sea una lista
        Recibe una lista que modifica
        Modifica segun el criterio de la funct
    '''
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if funct(lista[i],lista[j]):
                swaps_valores(lista,i,j)

def swaps_valores(lista:list,i:int,j:int)->None:
    '''
        Recibe una lista 
        Se encarga de swappear tanto lo que viene en i y j
    '''
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux 

def comprar_items(funct, lista:list)->dict:   
    '''
        Recibe una lista de la cual filtra dependiendo del lambda
        Retorna un elemento
    '''  
    validar_lista(lista)
    if(len(lista) > 0):
        bandera = True     
        for i in lista:         
            if bandera or funct(i, item):             
                bandera = False
                item = i
        return item
    return None



#Funciones especificas
def menu():
    """Es un menu que nos retorna un numero del menu"""
    print("""
    1 - Cargar archivo CSV.
    2 - Imprimir lista.
    3 - Asignar estadísticas.
    4 - Filtrar por mejores posts.
    5 - Filtrar por haters.
    6 - Informar promedio de followers.
    7 - Ordenar los datos por nombre de user ascendente.
    8 - Mostrar más popular.
    9 - Salir.
    """)
    return input("\nSeleccione una opcion del menu : \n")

def cargar_csv_msjExito(nombre_archivo):
    '''Carga el archivo'''
    return cargar_csv(nombre_archivo)

def imprimir_lista_influencers(lista_original_influencers):
    '''Muestra la lista de los influencers'''
    mostrar_influencers(lista_original_influencers)

def dar_estadisticas_influencer(lista_original_influencers):
    '''Mapea la lista de influencers dandole estadistitcas aleatorias'''
    return mapear_lista(asignar_estadisticas_aleatorios,lista_original_influencers)

def filtrar_por_mejores_posts(lista_estadisticas):
    '''Guarda el archivo csv filtrando la lista por mayor a 2000 likes'''
    guardar_csv("posts_2000_likes",filtrar_lista(lambda influencer: influencer["likes"] > 2000,lista_estadisticas))

def filtrar_por_haters(lista_estadisticas):
    '''Guarda el archivo csv filtrando la lista por si los dislikes son mayores que los likes'''
    guardar_csv("posts_con_haters",filtrar_lista(lambda influencer: influencer["dislikes"] > influencer["likes"],lista_estadisticas))

def informar_promedio_de_followers(lista_estadisticas):
    '''Muentra en terminal el promedio filtrando la lista por la clave followers'''
    lista_followers = filtrar_clave("followers",lista_estadisticas)
    promedio_followers = promedio_lista(lista_followers)
    print(f"El promedio en followers: {promedio_followers}")

def ordenar_los_datos_por_nombre_de_user_ascendente(lista_estadisticas):
    '''Ordena la lista por la clave user de manera ascendente'''
    orden_lista(lambda inf_uno,inf_dos: inf_uno["user"] > inf_dos["user"],lista_estadisticas)
    guardar_json("posts_ordenados_user_ascendente",lista_estadisticas)

def mostrar_mas_popular(lista_estadisticas):
    '''Te entrega al mejor influencer segun sus likes'''
    influencer_popular = comprar_items(lambda inf_uno, inf_dos: inf_uno["likes"] > inf_dos["likes"],lista_estadisticas)
    print(f"El influencer mas polular {influencer_popular["user"]} con {influencer_popular["likes"]} likes")