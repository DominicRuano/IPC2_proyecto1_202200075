from ListaSimple import ListaSimple
from XML import leerXML

obj = leerXML("entrada1.xml")
obj.getSenal()


valor = obj.listaDatos.getInicio()
print("8787887878")
while valor:
    valor.getDato().print()
    #print(valor.getDato().getTmax())
    #print(valor.getDato().getAmax())
    valor = valor.getSiguiente()




#obj.listaEncabezados.graficar()
obj.graficar2(0)
#obj.graficar2(1)
#obj.graficar2(2)