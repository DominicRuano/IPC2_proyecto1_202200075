import xml.etree.ElementTree as ET
from senal import senal
from ListaSimple import ListaSimple

class leerXML:
    def __init__(self, path) -> None:
        self.root = ET.parse(path).getroot()
        self.listaEncabezados = ListaSimple()
    
    def getSenal(self) -> None:
        self.listaEncabezados = ListaSimple()
        for a in self.root.findall("senal"):
            senal1 = a.get("nombre")
            Tmax =  a.get("t")
            Amax = a.get("A")
            tmpS = senal(senal1, Tmax, Amax)
            self.listaEncabezados.agregarFinal(tmpS)
        senguar = self.listaEncabezados.getInicio()
    
    def getDato(self):
        pass

    def getLista(self):
        return self.listaEncabezados