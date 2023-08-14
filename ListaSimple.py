class Nodo():
    def __init__(self,id, dato):
        self.id = id
        self.dato = dato
        self.siguiente = None

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getDato(self):
        return self.dato
    
    def setDato(self, dato):
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

class ListaSimple():
    id = 0
    def __init__(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

    def estaVacia(self):
        return self.nodoInicio == None

    def agregarFinal(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size += 1