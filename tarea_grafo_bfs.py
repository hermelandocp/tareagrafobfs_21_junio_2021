
class Grafo:
    arbol_bfs ={}
    def __init__(self, list_entrada={}):
        "EL constructor acepta una lista de adyacencia de entrada, si el usuario no da el parámetro se crea un garfo vacio"
        self.lista_ady = list_entrada


    def agrega_vertice_y_sus_adyacencias(self,nom_nodo, adyacencias):
        """Se agrega un método para agregar un nuevo vértice en el grafo con parametros de entrada nombre del nodo y
        una lista de adyacencias"""
        if nom_nodo in self.lista_ady:
            print("Ya ha sido dado de alta un nodo con este nombre, por favor cambie el nombre")
        else:
            self.lista_ady[nom_nodo] = adyacencias

    def elimina_vertice(self, nom_nodo):
        "Método que elimina un nodo y su lista de adyacencias"
        self.lista_ady.pop(nom_nodo)

    def agrega_adyacencia(self, nom_nodo, ady):
        "Agrega adyacencia a un vertice"
        self.lista_ady[nom_nodo].append(ady)

    def elimina_adyacencia(self, nom_nodo, ady):
        "Elimina adyacencia a un vertice"
        self.lista_ady[nom_nodo].remove(ady)

    def imprime_grafo(self):
        for x, y in self.lista_ady.items():
            print(x+": ", y)

    def elimina_lista(self):
        self.lista_ady={}

    def escribe_grafo_en_archivo(self, archivo):
        f = open(archivo, "a")
        f.write("lista_ady = "+ str(self.lista_ady))
        f.close()
    def bfs (self,nom_nodo):
        color = {}
        distancia = {}
        pred ={}
        q = list()
        for x in self.lista_ady:
          if x == nom_nodo:
            color[x]='gray'
            distancia[x]= 0
            pred[x]= []
            q.append(nom_nodo)
          else: 
            color[x]='white'
            distancia[x]= 9999
            pred[x]= []
      

        while len(q) > 0:

            u = q.pop()

            for v in self.lista_ady[u]:
                if color[v] == 'white':
                    color[v] = 'gray'
                    distancia[v] = distancia[u] + 1
                    pred[v]= u
                    q.append(v)
                    color[u]='black'
                    self.arbol_bfs = pred
                    print(pred)
                    return pred, distancia

    def imprime_ruta (Grafo, self,x, u):
      if u == x:
        print(x)
      else:
        if pred[u] == []:
          print('No hay camino', x, 'hacia', u)
        else:
          print(u)

nom_nodo='x'
adyacencias=["t","u","w","y"]
grafo1= Grafo()
grafo1.agrega_vertice_y_sus_adyacencias( nom_nodo, adyacencias)
grafo1.agrega_vertice_y_sus_adyacencias("r",["s","v"])
grafo1.agrega_vertice_y_sus_adyacencias("s",["r","w"])
grafo1.agrega_vertice_y_sus_adyacencias("t",["w","x","u"])
grafo1.agrega_vertice_y_sus_adyacencias("u",["t","x","y"])
grafo1.agrega_vertice_y_sus_adyacencias("v",["r"])
grafo1.agrega_vertice_y_sus_adyacencias("w",["s","t","x"])
grafo1.agrega_vertice_y_sus_adyacencias("y",["x","u"])
grafo1.bfs(nom_nodo)
grafo1.imprime_grafo()