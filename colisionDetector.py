import math
class Colision:
    def comprobar(self,lista):
        for elementoI in lista:
            for elementoJ in lista:
                if elementoI!=elementoJ:
                    distancia = self.getDistancia(elementoI,elementoJ)
                    if distancia < elementoI.getRadio() * 2 * 1.0:
                        elementoI.setFuerza(self.normal(elementoJ, elementoI), elementoI.getRadio() * 2.0 - distancia)
                        elementoJ.setFuerza(self.normal(elementoI, elementoJ), elementoI.getRadio() * 2.0 - distancia)

    def getDistancia(self, elementoI, elementoJ):
        return math.sqrt(math.pow(elementoI.getPos()[0]-elementoJ.getPos()[0], 2)+math.pow(elementoI.getPos()[1]-elementoJ.getPos()[1], 2))

    def suelo(self, lista, suelo):
        for elemento in lista:
            if elemento.getPos()[1]+elemento.getRadio()>suelo:
                elemento.setFuerza([0, -1], elemento.getPos()[1]+elemento.getRadio()-suelo)
    def pared(self, lista, pared1, pared2):
        for elemento in lista:
            if elemento.getPos()[0]-elemento.getRadio()<pared1:
                elemento.setFuerza([1, 0], elemento.getPos()[0]-elemento.getRadio()-pared1)
            if elemento.getPos()[0]+elemento.getRadio()>pared2:
                elemento.setFuerza([-1, 0], elemento.getPos()[0]+elemento.getRadio()-pared2)

    def normal(self, i, j):
        vector = [j.getPos()[0]-i.getPos()[0], j.getPos()[1]-i.getPos()[1]]
        # print(vector)
        modulo = math.sqrt(math.pow(vector[0], 2)+math.pow(vector[1], 2))
        if modulo != 0:
            return [vector[0]/modulo, vector[1]/modulo]
        else:
            return [999999, 999999]
