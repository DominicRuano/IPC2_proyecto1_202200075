from ListaSimple import ListaSimple
from XML import leerXML

obj = leerXML("entrada1.xml")
obj.getSenal()

valor = obj.listaEncabezados.getInicio()
print("8787887878")
while valor:
    print(valor.getDato().getNombre())
    valor = valor.getSiguiente()