class dato:
    def __init__(self, tiempo, amplitud, dato, senal) -> None:
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.dato = dato
        self.senal = senal
    
    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def getDato(self):
        return self.dato
    
    def getSenal(self):
        return self.senal
    
    def print(self):
        print("___SENAL: {} | Tiempo: {} | Amplitud: {} | Dato: {} ___".format( self.senal, self.tiempo, self.amplitud, self.dato))