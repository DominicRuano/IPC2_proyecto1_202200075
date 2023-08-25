import graphviz

class Graph():
    def __init__(self):
        self.dot = graphviz.Digraph('structs', filename='structs.gv', node_attr={'shape': 'record', 'fontname':'Helvetica'})    

    def add(self, nodoInicio, nodoSiguiente):
        if(nodoSiguiente):
            self.dot.node(str(nodoInicio.getDato().getNombre()), str(nodoInicio.getDato().getNombre()))
            self.dot.node(str(nodoSiguiente.getDato().getNombre()), str(nodoSiguiente.getDato().getNombre()))
            self.dot.edge(str(nodoInicio.getDato().getNombre()), str(nodoSiguiente.getDato().getNombre()))
    
    def addEncabezado(self, NombreSenal):
        self.dot.node(str(NombreSenal.getDato().getNombre()), str(NombreSenal.getDato().getNombre()))
        self.dot.node("T= "+str(NombreSenal.getDato().getTmax()), "T= "+str(NombreSenal.getDato().getTmax()))
        self.dot.edge(str(NombreSenal.getDato().getNombre()), "T= "+str(NombreSenal.getDato().getTmax()))

        self.dot.node(str(NombreSenal.getDato().getNombre()), str(NombreSenal.getDato().getNombre()))
        self.dot.node("A= "+str(NombreSenal.getDato().getAmax()), "A= "+str(NombreSenal.getDato().getAmax()))
        self.dot.edge(str(NombreSenal.getDato().getNombre()), "A= "+str(NombreSenal.getDato().getAmax()))
    
    def addNodo(self, nodoInicio, nodoSiguiente, random):
        if(nodoSiguiente and nodoSiguiente.getDato().getSenal() == nodoInicio.getDato().getSenal()):
                    self.dot.node(str(random), str(nodoInicio.getDato().getDato()))
                    self.dot.node(str(random + 1), str(nodoSiguiente.getDato().getDato()))
                    self.dot.edge(str(random), str(random + 1))

    def generar(self):
        self.dot.render(outfile='img/structs.png').replace('\\', '/')
        'img/structs.png' 
    
    def generar2(self,a):
        nombre = "img/structs{}.png".format(a)
        self.dot.render(outfile=nombre).replace('\\', '/')
        'img/structs.png' 