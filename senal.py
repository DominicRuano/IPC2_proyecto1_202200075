from ListaSimple import ListaSimple
from tiempo import tiempo

class senal:
    def __init__(self, nombre, Tmax, Amax) -> None:
        self.nombre = nombre
        self.tmax = Tmax
        self.amax = Amax
        self.tiempos = ListaSimple()
        self.listatiempo()
    
    def getNombre(self):
        return self.nombre
    
    def getTmax(self):
        return self.tmax
    
    def getAmax(self):
        return self.amax
    
    def listatiempo(self):
        for i in range(1, int(self.tmax) + 1):
            objT = tiempo(i, self.amax)
            self.tiempos.agregarFinal(objT)