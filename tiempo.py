from ListaSimple import ListaSimple
from amplitud import amplitud

class tiempo:
    def __init__(self, tiempo, amplitud) -> None:
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.amplitudes = ListaSimple()
        self.listaAmplitudes()
    
    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def listaAmplitudes(self):
        for a in range(1, int(self.amplitud) + 1):
            tmp = amplitud(a)
            self.amplitudes.agregarFinal(tmp)

