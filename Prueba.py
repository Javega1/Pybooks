
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def menu_inicial():
    while True:
        print("\n****Menú de inicio****")
        print("1.- Stock marca.")
        print("2.- Búsqueda por precio..")
        print("3.- Actualizar precio.")
        print("4.- Salir.")
        opcion=input("Ingrese su opción: ")
        
        match opcion:
            case "1":
                stockMarca()
            case "2":
                "Hola"
                busquedaPorPrecio()
            case "3":
               actualizarPrecio()
            case "4":
                print("Pro-grama finalizado.")
                break
            case _:
                print("Opción incorrecta. Por favor, vuelva a intentar.")
                

def stockMarca():
    while True:
        marcaConsulta = input("Ingre marca a consultar ")
        for i in productos:
            for c in productos[i]:
                if marcaConsulta == c:
                    marcafiltro = c
                    for j in marcafiltro,1:
                        marcafiltro = i 
        for i in stock:
            print(marcafiltro)
            if marcafiltro == i:
                stockfiltro = i  
                    
def busquedaPorPrecio():
    print("Revisar")

def actualizarPrecio():
    print("Revisar")
                     
  
menu_inicial()

