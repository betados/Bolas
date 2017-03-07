
class ListaBolas:
    lista = []
    def add(self, bola):
        self.lista.append(bola)

    def dibuja(self,color):
        for grano in self.lista:
            grano.dibuja(color)

    def actualiza(self,t):
        for grano in self.lista:
            grano.actualiza(t)

    def  getLista(self):
        return self.lista