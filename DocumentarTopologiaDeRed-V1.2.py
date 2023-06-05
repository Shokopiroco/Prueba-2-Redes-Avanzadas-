import os
import time
import ipaddress

listas = []

def leer():
    archivo = 'planilla5.txt'
    try:
        with open(archivo, 'r') as file:
            contents = file.read()
            print(contents)
            time.sleep(2)
            while True:
                print("Desea prolongar su sesion de lectura? \nSi.\tNo.")
                sesion = input()
                if sesion == "si" or sesion == "Si":
                    os.system("clear")
                    print(contents)
                    time.sleep(2)
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

def generador_lista():
    while True:
        lista = []
        while True:
            i = 0
            zona = input("Ingrese nombre de la zona en que operan los dispositivos: "); i = i + 1
            dispositivo = input("Ingrese dispositivo que pertenece a la zona: "); i = i + 1
            interfaz = input("Ingrese la interfaz conectada:\n(SERIAL/FASTETH/GIGABIT/ETHER)(X/X) o (X/X/X): "); i = i + 1
            while True:
                direccion_ip = input("Ingrese la direccion ip de la interfaz antes mencionada: ")
                if validador_IP(direccion_ip):
                    i = i + 1
                    break
                else:
                    print("Direccion IP invalida. Favor de ingresar una direccion IP valida.")
            while True:
                mascara = int(input("Ingrese mascara de red en la que trabaja la interfaz: "))
                if mascara > 0 and mascara <= 32:
                    mascara = str(mascara)
                    i = i + 1
                    break
                elif mascara <= 0 or mascara > 30:
                    print("La mascara de red ha sido ingresada erroneamente.")
            destino = input("Ingrese nombre del dispositivo de destino: "); i = i + 1
            capa_jerarquica = input("Ingrese la capa jerarquica perteneciente al equipo: "); i = i + 1
            servicio_adheridos = input("Ingrese los servicios que estan disponibles en el dispositivo: "); i = i + 1
            protocolos_de_red = input("Ingrese los protocolos de enrutamiento del dispositivo: "); i = i + 1
            lista.append([zona, dispositivo, interfaz, direccion_ip, "/" + mascara, destino, capa_jerarquica, protocolos_de_red, servicio_adheridos]); i = i + 1
            if i == 10:
                break
        listas.append(lista)
        os.system("clear")
        while True:
            agregar = input("Desea agregar una nueva interfaz? (S/N) ")
            if agregar == "Si" or agregar == "si" or agregar == "SI" or agregar == "S" or agregar == "s":
                zona = ""
                dispositivo = "\t"
                interfaz = input("Ingrese la interfaz conectada:\n(SERIAL/FASTETH/GIGABIT/ETHER)(X/X) o (X/X/X): ")
                while True:
                    direccion_ip = input("Ingrese la direccion ip de la interfaz antes mencionada: ")
                    if validador_IP(direccion_ip):
                        break
                    else:
                        print("Direccion IP invalida. Favor de ingresar una direccion IP valida.")
                while True:
                    mascara = int(input("Ingrese mascara de red en la que trabaja la interfaz: "))
                    if mascara >= 0 and mascara <= 32:
                        mascara = str(mascara)
                        break
                    elif mascara < 0 or mascara > 32:
                        print("La mascara de red ha sido ingresada erroneamente.")
                destino = input("Ingrese nombre del dispositivo de destino: ")
                capa_jerarquica = "\t"
                servicio_adheridos = "\t"
                protocolos_de_red = "\t"
                lista.append([zona, dispositivo, interfaz, direccion_ip, "/" + mascara, destino, capa_jerarquica, protocolos_de_red, servicio_adheridos])
            elif agregar == "N" or agregar == "n" or agregar == "no" or agregar == "NO" or agregar == "No":
                break
        os.system("clear")
        continuar = input("¿Deseas crear otra lista? (s/n): ")
        if continuar.lower() != "s":
            break

def reemplazar():
    archivo = 'planilla5.txt'
    with open(archivo, 'r') as file:
        contents = file.read()
        print(contents)
        antiguo = input("Ingrese el texto que desea reemplazar: ")
        nuevo = input("Ingrese el nuevo texto para reemplazar: ")
        ocurrencias = contents.count(antiguo)
        if ocurrencias == 0:
            print("El texto especificado no se encontró en el archivo.")
            return
        while True:
            numero_texto = input(f"Ingrese el número correspondiente al texto que desea cambiar (1-{ocurrencias}): ")
            if numero_texto.isdigit() and 1 <= int(numero_texto) <= ocurrencias:
                numero_texto = int(numero_texto)
                break
            else:
                print("Número inválido. Intente nuevamente.")
        index = contents.find(antiguo)  # Encuentra la primera ocurrencia del texto antiguo
        for _ in range(numero_texto - 1):
            index = contents.find(antiguo, index + len(antiguo))  # Encuentra la ocurrencia deseada
        contents = contents[:index] + nuevo + contents[index+len(antiguo):]
    with open(archivo, 'w') as file:
        file.write(contents)
    print("Texto reemplazado en el archivo " + archivo)


def menu():
    os.system("clear")
    print("--------------MENU-------------------")
    print("1. Leer archivo planilla5.txt")
    print("2. Agregar al archivo planilla5.txt")
    print("3. Reemplazar texto en archivo planilla5.txt")
    print("4. Salir.")
    print("\n\n---------------------------------")

while True:
    menu()
    opc = input("Ingrese la opción que desea realizar: ")
    if opc == "1":
        leer()
    elif opc == "2":
        generador_lista()
        for i, lista in enumerate(listas):
            print("Lista", i + 1, ":", lista)
        with open('planilla5.txt', 'a') as file:
            for lista in listas:
                for item in lista:
                    file.write('\t'.join(item) + '\n')
        print("Datos agregados al archivo planilla5.txt")
        listas = []
    elif opc == "3":
        reemplazar()
    elif opc == "4":
        print("Saliendo del programa...")
        time.sleep(3)
        break
    else:
        print("Opción inválida. Intente nuevamente.")