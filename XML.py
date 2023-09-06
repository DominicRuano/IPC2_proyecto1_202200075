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
                if 0 < int(tiempo) <= 3600 and 0 < int(amplitud) <= 130:
                    self.listaDatos.agregarFinal(tmpD)
                if int(dato2) > 0:
                    tmpB = dato(tiempo,amplitud,"1", senal1)
                    if 0 < int(tiempo) <= 3600 and 0 < int(amplitud) <= 130:
                        self.listaBinaria.agregarFinal(tmpB)
                else:
                    tmpB = dato(tiempo,amplitud,"0", senal1)
                    if 0 < int(tiempo) <= 3600 and 0 < int(amplitud) <= 130:
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

    def graficar3(self, valor):
        valor1 = 1
        graph = Graph()
        tmp = self.listaEncabezados.nodoInicio
        primerNodo = self.listaBinaria.nodoInicio
        segundoNodo = primerNodo.getSiguiente()
        for a in range(self.listaEncabezados.size):
            if a == valor:
                graph.addEncabezado(tmp)
                primerNodoC = primerNodo
                segundoNodoC = segundoNodo
                for amplitud in range(1, int(tmp.getDato().getAmax()) + 1):
                    for amplitud2 in range(1, int(self.listaBinaria.size) + 1):
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
                graph.generar2("{} binario".format(a))
                return
            tmp = tmp.getSiguiente()

    def generarArchivo(self):
        with open("salida.xml", "w") as f:
            f.write("<?xml version=\"1.0\"?>\n")
            f.write("<SenalesBinarios>\n")
            tmp = self.listaEncabezados.nodoInicio
            while tmp:
                print(tmp.getDato().getNombre())
                f.write("\t<senal nombre=\"{}\" t=\"{}\" A=\"{}\">\n".format(tmp.getDato().getNombre(), tmp.getDato().getTmax(), tmp.getDato().getAmax()))
                tmp2 = self.listaBinaria.nodoInicio
                while tmp2:
                    print(tmp2.getDato().getSenal())
                    if tmp.getDato().getNombre() == tmp2.getDato().getSenal():
                        f.write("\t\t<dato t=\"{}\" A=\"{}\">{}</dato>\n".format(tmp2.getDato().getTiempo(), tmp2.getDato().getAmplitud(), tmp2.getDato().getDato()))
                    tmp2 = tmp2.getSiguiente()
                f.write("\t</senal>\n")
                tmp = tmp.getSiguiente()
            f.write("</SenalesBinarios>\n")