import xml.etree.ElementTree as ET
from senal import senal
from dato import dato
from ListaSimple import ListaSimple
from graph import Graph

class leerXML:
    def __init__(self, path) -> None:
        self.root = ET.parse(path).getroot()
        self.listaEncabezados = ListaSimple()
        self.listaDatos = ListaSimple()
    
    def getSenal(self) -> None:
        #self.listaEncabezados = ListaSimple()
        for a in self.root.findall("senal"):
            
            senal1 = a.get("nombre")
            Tmax =  a.get("t")
            Amax = a.get("A")
            tmpS = senal(senal1, Tmax, Amax)
            self.listaEncabezados.agregarFinal(tmpS)

            for e in a.findall("dato"):
                tiempo = e.get("t")
                amplitud = e.get("A")
                dato2 = e.text 
                tmpD = dato(tiempo,amplitud,dato2, senal1)
                self.listaDatos.agregarFinal(tmpD)

        senguar = self.listaEncabezados.getInicio()

    def getLista(self):
        return self.listaEncabezados
    
    def graficar2(self, valor):
        valor1 = 1
        graph = Graph()
        tmp = self.listaEncabezados.nodoInicio
        while tmp:
            for a in range(self.listaEncabezados.size):
                if a == valor:
                    graph.addEncabezado(tmp)
                    
                    primerNodo = self.listaDatos.nodoInicio
                    primerNodoC = primerNodo
                    segundoNodo = self.listaDatos.nodoInicio.getSiguiente()
                    segundoNodoC = segundoNodo 
                    for b in range(1, int(tmp.getDato().getAmax()) + 1):
                        while segundoNodo and primerNodo.getDato().getAmplitud() == str(b) :
                            print(primerNodo.getDato().getAmplitud() == str(b) and  segundoNodo.getDato().getAmplitud() == str(b))
                            print("----")
                            if primerNodo.getDato().getAmplitud() == str(b) and  segundoNodo.getDato().getAmplitud() == str(b) and primerNodo.getDato().getSenal() == segundoNodo.getDato().getSenal():
                                graph.addNodo(primerNodo, segundoNodo,valor1, b)
                                valor1 += 1
                                #primerNodo = primerNodo.getSiguiente()
                                primerNodo = segundoNodo
                                segundoNodo = segundoNodo.getSiguiente()
                            else:
                                segundoNodo = segundoNodo.getSiguiente()
                        primerNodo = primerNodoC.getSiguiente()
                        segundoNodo = segundoNodoC.getSiguiente()
                    graph.generar2(a)
                    return
                tmp = tmp.getSiguiente()