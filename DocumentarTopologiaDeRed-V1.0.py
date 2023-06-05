import os
import time
import ipaddress # Para intrducior direcciones IP

listas = []# Crear una lista vacía para almacenar las listas de elementos
#matriz = ["ZONA","\t","DISPOSITIVO","\t","INTERFAZ","\t","IP","\t","\t","MASCARA","\t","\t","DESTINO","\t","\t","CAPA JERÁRQUICA","\t","PROTOCOLOS DE RED","\t","SERVICIOS DE RED","\n"]#encabezado de la documentacion
#listas.append(matriz)

def leer():
    archivo = 'planilla5.txt'
    try:
        with open(archivo, 'r') as file:
            contents = file.read()
            print(contents)
            time.sleep(10)
            while True:
                print("Desea prolongar su sesion de lectura? \nSi.\tNo.")
                sesion = input()
                if sesion == "si" or sesion == "Si":
                    os.system("clear")
                    print(contents)
                    time.sleep(10)
                elif sesion == "no" or sesion == "No":
                    opc = 9
                    break
    except FileNotFoundError:
        print("Archivo no encontrado.\nRegresando...")
        time.sleep(3)

def validador_IP(direccion_ip):
    try:
        ipaddress.ip_address(direccion_ip)
        return True
    except ValueError:
        return False

def generador_lista():# Solicitar al usuario que ingrese elementos
    while True:
        lista = []  # Crear una nueva lista vacía para cada iteración
        while True:
            i = 0
            zona = input("Ingrese nombre de la zona en que operan los dispositivos: "); i = i +1 #zona en la que trabajan los equipos
            dispositivo = input("Ingrese dispositivo que pertenece a la zona: "); i = i +1 #nombre del dispositivo
            interfaz = input("Ingrese la interfaz conectada:\n(SERIAL/FASTETH/GIGABIT/ETHER)(X/X) o (X/X/X): "); i = i +1 #numero de interfaz
            while True:
                direccion_ip = input("Ingrese la direccion ip de la interfaz antes mencionada: "); #direccion ip de la interfaz
                if validador_IP(direccion_ip):
                    i = i +1
                    break
                else:
                    print("direccion ip invalida. Favor de ingresar un direccion ip valida.")
            while True:
                mascara = int(input("Ingrese mascara de red en la que trabaja la interfaz: "))#Mascara de red de la interfaz
                if mascara > 0 and mascara <= 32:
                    mascara = str(mascara)
                    i = i + 1 #Mascara de red de la interfaz 
                    break
                elif mascara <= 0 or mascara > 30:
                    print("La mascara de red ha sido ingresada erroneamente.")
            destino = input("Ingrese nombre del dispositvo de destino: "); i = i + 1 #destino de la interfaz o hacia donde llegará esa interfaz
            capa_jerarquica = input("Ingrese la capa jerarquica perteneciente al equipo: "); i = i +1 #jerarquia perteneciente al equipo
            servicio_adheridos = input("Ingrese los servicios que estan disponibles en el dispositivo: "); i = i +1 #servicios que estan configurados en el equipo
            protocolos_de_red = input("Ingrese los protocolos de enrutamiento del dispositivo: "); i = i +1 #protocolos de red que tiene configurado el equipo
            lista.append(zona+"\t"+dispositivo+"\t"+interfaz+"\t"+direccion_ip+"\t"+"/"+mascara+"\t"+"\t"+destino+"\t"+capa_jerarquica+"\t"+"\t"+protocolos_de_red+"\t"+"\t"+servicio_adheridos+"\n"); i = i +1 #se agrega las variables a una lista
            if i == 10:
                break
        listas.append(lista)  # Agregar la lista actual a la matriz lista
        os.system("clear")
        while True:
            agregar = input("Desea agregar una nueva interfaz? (S/N) ") #se agrega interfaces adicionales del equipo en caso de tenerlas
            if agregar == "Si" or agregar == "si" or agregar == "SI" or agregar == "S" or agregar == "s":
                zona = ""
                dispositivo = "\t"
                interfaz = input("Ingrese la interfaz conectada:\n(SERIAL/FASTETH/GIGABIT/ETHER)(X/X) o (X/X/X): "); i = i +1 #numero de interfaz
                while True:
                    direccion_ip = input("Ingrese la direccion ip de la interfaz antes mencionada: "); #direccion ip de la interfaz
                    if validador_IP(direccion_ip):
                        i = i +1
                        break
                    else:
                        print("direccion ip invalida. Favor de ingresar un direccion ip valida.")
                while True:
                    mascara = int(input("Ingrese mascara de red en la que trabaja la interfaz: "))#Mascara de red de la interfaz
                    if mascara >= 0 and mascara <= 32:
                        mascara = str(mascara)
                        break
                    elif mascara < 0 or mascara > 32:
                        print("La mascara de red ha sido ingresada erroneamente.")
                destino = input("Ingrese nombre del dispositvo de destino: ")
                capa_jerarquica ="\t"
                servicio_adheridos = "\t"
                protocolos_de_red = "\t"
                lista.append(zona+"\t"+dispositivo+"\t"+interfaz+"\t"+direccion_ip+"\t"+"/"+mascara+"\t"+"\t"+destino+"\t"+capa_jerarquica+"\t"+"\t"+protocolos_de_red+"\t"+"\t"+servicio_adheridos+"\n") #agrega una lista de la interfaz configurada 
            elif agregar == "N" or agregar == "n" or agregar == "no" or agregar == "NO" or agregar == "No":
                break
        os.system("clear")
        continuar = input("¿Deseas crear otra lista? (s/n): ") #creamos otra lista para otro dispositivo.
        if continuar.lower() != "s":
            break

def reemplazar():
    archivo = 'planilla5.txt'
    with open(archivo, 'r+') as file:
        contents = file.read()
        print(contents)
        antiguo = input("Ingrese el Texto que desea Reemplazar: ")
        nuevo = input("Ingrese el nuevo Texto para Reemplazar: ")
        ocurrencias = contents.count(antiguo)# Obtener todas las ocurrencias de "DISTRIBUCION"
        numero_texto = input(f"Ingrese el número correspondiente al texto que desea cambiar (1-{ocurrencias}): ") # Solicitar al usuario el número de texto a cambiar
        numero_texto = int(numero_texto)
        contents = contents.replace(antiguo, nuevo, numero_texto)
        file.seek(numero_texto)
        file.write(contents)
        file.truncate()
        print("Texto reemplazado en el Archivo " + archivo)

def menu():
    os.system("clear")
    print("--------------MENU-------------------")
    print("1. leer archivo backbone.txt")
    print("2. Agregar al archivo backbone.txt")
    print("3. Reemplazar Texto en archivo backbone.txt")
    print("4. Salir.")
    print("\n\n---------------------------------")

while True:
    menu()
    opc = int(input("Ingrese la opcion que desea realizar."))
    if opc == 1:
        leer()
    elif opc == 2:
        generador_lista()
        for i, lista in enumerate(listas): # Imprimir todas las listas creadas
            print("Lista", i + 1, ":", lista)
        with open('planilla5.txt', 'a') as archivo: #Guarda las listas en un archivo de texto.
            for fila in listas:
                for elements in fila:
                    archivo.write(elements)
    elif opc == 3:
        reemplazar()
    elif opc == 4:
        break