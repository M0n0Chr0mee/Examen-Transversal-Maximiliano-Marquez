#productos = {modelo: [marca, pantalla, ram, disco, gb de dd, procesador, video]...}
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'Integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'ADM Ryzen 5', 'Integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'ADM Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'ADM Ryzen 3', 'Nvidia GTX1050']}
#stock = {modelo: [precio, stock], ...}
stock = {'8475HD': [387990,10],
         '2175HD': [327990,4],
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21],
         'GF75HD': [290890,32],
         '123FHD': [444990,7],
         '342FHD': [749990,2],
         'UWU131HD': [349990,1],
         'FS1230HD': [249990,0]}
def stock_marca(marca):
    print("Stock de marca:", marca)
    total_stock = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower() and modelo in stock:
            total_stock += stock[modelo][1]
    print(f"El stock de las marcas disponibles son: {total_stock}")
def busqueda_precio(minimo, maximo):
    if not (isinstance(minimo, int)and isinstance(maximo, int)):
        print("Debe ingresar valores enteros!!")
        return
    resultados = []
    for modelo, datos in stock.items():
        precio = datos [0]
        if minimo <= precio <= maximo and datos[1] > 0:
            if modelo in productos:
                marca = productos[modelo][0]
                resultados.append(f"{marca}--{modelo}")
    if resultados:
        print("Los notebooks disponibles entre la consulta del limite de precio son: ", resultados)
    else:
        print("No hay notebooks en el rango de precio establecido")
def actualizar_precio(modelo, precio_actualizado):
    if modelo in stock:
        stock[modelo][0] = precio_actualizado
        return True
    else:
        return False

def menu():
    while True:
        print("***MENU PRINCIPAL***")
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir")
        opcion_menu = input("Ingrese una opcion:  ")
        if opcion_menu == "1":
            marca = input("Ingrese la marca que quiere consultar: ")
            stock_marca(marca)
        elif opcion_menu == "2":
            minimo = int(input("Seleccione el rango minimo de precio que estas buscando: "))
            maximo = int(input("Seleccione el rango maximo de precio que estas buscando: "))
            busqueda_precio(minimo, maximo)
        elif opcion_menu == "3":
            while True:
                modelo = input("Ingrese el modelo que desea actualizar: ").strip
                if modelo in stock:
                    try:
                        precio_actualizado = int(input("Ingrese el precio nuevo para el equipo: "))
                        if actualizar_precio(modelo, precio_actualizado):
                            print("Precio actualizado!!")
                        else:
                            print("Error al actualizar")
                    except ValueError:
                        print("Debe ingresar un precio valido!!!")
                else:
                    print("El modelo no existe!!")
                continuar = input("Desea continuar actualizando precios? (Y/N)")
                if continuar != "n":
                 break
        elif opcion_menu == "4":
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar una opcion válida!!")
menu()