from XML import leerXML
import os

def cargarArchivo() -> str:
    print("Opcion cargar archivos:")
    nombre = input("Ingrese el nombre del archivo (sin .xml): ") + ".xml"

    if input("¿seguro que el nombre {} es correcto? (s/n): ".format(nombre)) == "s":
        return nombre

    else:
        return cargarArchivo()




#Inicio del programa
nombreArchivo = None
obj = None

os.system("cls")
while True:
    print("Menu Principal:")
    print("     1. Cargar Archivo")
    print("     2. Procesar Archivo")
    print("     3. Escribir Archivo Salida")
    print("     4. Mostrar Datos del Estudiante")
    print("     5. Generar Grafica")
    print("     6. Inicializar Sistema")
    print("     7. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        os.system("cls")
        nombreArchivo = cargarArchivo()
        print("archivo cargado con exito!")

    elif opcion == "2":
        os.system("cls")
        print("Procesar Archivo")
        if nombreArchivo:
            obj = leerXML(nombreArchivo)
            print("calculando la matriz binaria...")
            print("calculando la suma de tuplas...")
            obj.getSenal()
        else:
            print("No se ha cargado un archivo, por favor cargue un archivo primero")

    elif opcion == "3":
        os.system("cls")
        if obj:
            print("Escribir Archivo Salida")
            obj.escribirArchivoSalida()
        else:
            print("No se ha cargado un archivo, por favor cargue un archivo primero")
        #escribirArchivoSalida()

    elif opcion == "4":
        os.system("cls")
        print("Mostrar Datos del Estudiante:")
        print(">    Dominic juan pablo Ruano Perez")
        print(">    202200075")
        print(">    Introduccion a la Programacion y Computacion 2 seccion \"A\"")
        print(">    Ingenieria en Ciencias y Sistemas")
        print(">    4to Semestre")
        #mostrarDatosEstudiante()

    elif opcion == "5":
        os.system("cls")
        if obj:
            print("Generar Grafica:")
            tmp = obj.listaEncabezados.nodoInicio
            for a in range(obj.listaEncabezados.size):
                print(">     {}. {}".format(a+1, tmp.getDato().getNombre()))
                tmp = tmp.getSiguiente()
            opcion = input("Ingrese la senal de la cual desea generar la grafica: ")
            obj.graficar2(int(opcion)-1)
        else:
            print("No se ha cargado un archivo, por favor cargue un archivo primero")

    elif opcion == "6":
        os.system("cls")
        print("Inicializar Sistema")
        #inicializarSistema()

    elif opcion == "7":
        os.system("cls")
        print("Saliendo...")

    else:
        os.system("cls")
        print("Opcion invalida")

#obj.listaEncabezados.graficar()
#obj.graficar2(0)
#obj.graficar2(1)
#obj.graficar2(2)
