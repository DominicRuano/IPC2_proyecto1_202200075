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
        self.listaBinaria = ListaSimple()
    
    def getSenal(self) -> None:
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
                if int(dato2) > 0:
                    tmpB = dato(tiempo,amplitud,"1", senal1)
                    self.listaBinaria.agregarFinal(tmpB)
                else:
                    tmpB = dato(tiempo,amplitud,"0", senal1)
                    self.listaBinaria.agregarFinal(tmpB)

        senguar = self.listaEncabezados.getInicio()

    def getLista(self):
        return self.listaEncabezados
    
    def graficar2(self, valor):
        valor1 = 1
        graph = Graph()
        tmp = self.listaEncabezados.nodoInicio
        primerNodo = self.listaDatos.nodoInicio
        segundoNodo = primerNodo.getSiguiente()

        for a in range(self.listaEncabezados.size):
            if a == valor:
                graph.addEncabezado(tmp)
                primerNodoC = primerNodo
                segundoNodoC = segundoNodo
                for amplitud in range(1, int(tmp.getDato().getAmax()) + 1):
                    for amplitud2 in range(1, int(self.listaDatos.size) + 1):
                            if segundoNodoC:
                                if tmp.getDato().getNombre() == primerNodoC.getDato().getSenal():
                                    if primerNodoC.getDato().getSenal() == segundoNodoC.getDato().getSenal():
                                        if primerNodoC.getDato().getAmplitud() == segundoNodoC.getDato().getAmplitud():
                                            graph.addNodo(primerNodoC, segundoNodoC, valor1)
                                            valor1 += 1
                                            primerNodoC = segundoNodoC
                                            segundoNodoC = segundoNodoC.getSiguiente()
                                        else:
                                            segundoNodoC = segundoNodoC.getSiguiente()
                                else:
                                    primerNodoC = primerNodo.getSiguiente()
                                    segundoNodoC = primerNodoC.getSiguiente()
                                    primerNodo = primerNodo.getSiguiente()
                                    valor1 += 2
                    primerNodoC = primerNodo.getSiguiente()
                    segundoNodoC = primerNodoC.getSiguiente()
                    primerNodo = primerNodo.getSiguiente()
                    valor1 += 2
                graph.generar2(a)
                return
            tmp = tmp.getSiguiente()