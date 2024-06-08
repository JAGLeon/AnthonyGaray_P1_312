from funciones_influencers import *

primer_paso = False
segundo_paso = False

while True:
    match menu():
        case "1":
            lista_influencers = cargar_csv_msjExito("posts")
            primer_paso = True
        case "2":
            if primer_paso:
                imprimir_lista_influencers(lista_influencers)
            else:
                print("\nDebe cargar archivo CSV\n")
        case "3":
            if primer_paso:
                lista_estadisticas = dar_estadisticas_influencer(lista_influencers)
                segundo_paso = True
            else:
                print("\nDebe cargar archivo CSV\n")
        case "4":
            if segundo_paso:
                filtrar_por_mejores_posts(lista_estadisticas)
            else:
                print("\nDebe asignar estadísticas\n")
        case "5":
            if segundo_paso:
                filtrar_por_haters(lista_estadisticas)
            else:
                print("\nDebe asignar estadísticas\n")
        case "6":
            if segundo_paso:
                informar_promedio_de_followers(lista_estadisticas)
            else:
                print("\nDebe asignar estadísticas\n")
        case "7":
            if primer_paso:
                ordenar_los_datos_por_nombre_de_user_ascendente(lista_influencers)
            else:
                print("\nDebe cargar archivo CSV\n")
        case "8":
            if segundo_paso:
                mostrar_mas_popular(lista_estadisticas)
            else:
                print("\nDebe asignar estadísticas\n")
        case "9":
            break

