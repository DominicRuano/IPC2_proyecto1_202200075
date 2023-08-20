import xml.etree.ElementTree as ET
from senal import senal
from ListaSimple import ListaSimple

class leerXML:
    def __init__(self, path) -> None:
        self.root = ET.parse(path).getroot()
    
    def getSenal(self) -> None:
        listsenales = ListaSimple()
        for a in self.root.findall("senal"):
            senal1 = a.get("nombre")
            Tmax =  a.get("t")
            Amax = a.get("A")
            tmpS = senal(senal1, Tmax, Amax)
            listsenales.agregarFinal(tmpS)
        print("Lista de senales:")
        senguar = listsenales.getInicio()
        while senguar:
            print(senguar.getDato().getNombre())
            senguar = senguar.getSiguiente()
    
    def getDato(self):
        pass

obj = leerXML("entrada1.xml")
obj.getSenal()