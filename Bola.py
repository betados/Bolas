import pygame
import random
import math
class Bola:
    pantalla=0
    color=0
    radio=20
    acel= [0.0, 0.0]
    vel = [0.0, 0.0]
    normal = [0.0, 0.0]
    g= 0.0, 0.001
    k=0.01
    fuerza = 0.0 , 0.0
    # superposicion = 0.0
    aerodinamica=0.003

    listaFuerzas = []


    def __init__(self,pantalla):
        self.pantalla=pantalla
        self.pos = pygame.mouse.get_pos()
        self.color =[random.randrange(255), random.randrange(255), random.randrange(255)]
        # self.masa = 8
        self.masa = math.pow(self.radio, 3)*0.001

    def actualiza(self, t):
        # fuerzaElasica = self.k * self.superposicion
        # self.fuerza = fuerzaElasica * self.normal[0], fuerzaElasica * self.normal[1] + self.g[1]
        fuerzaElastica=self.getFuerza()
        if self.vel[0]>0:
            multX=-1
        else:
            multX=1
        if self.vel[1] > 0:
            multY = -1
        else:
            multY = 1
        fuerzaAerodinamica = math.pow(self.vel[0], 2) * self.aerodinamica * multX, math.pow(self.vel[1], 2) * self.aerodinamica * multY
        self.fuerza = fuerzaElastica[0]+self.g[0] + fuerzaAerodinamica[0], fuerzaElastica[1]+self.g[1] + fuerzaAerodinamica[1]
        # print(self.fuerza)
        self.acel = self.fuerza[0]/self.masa,  self.fuerza[1]/self.masa
        self.vel = self.vel[0]+0.5*self.acel[0]*t*t, self.vel[1]+0.5*self.acel[1]*t*t
        self.pos = self.pos[0] + self.vel[0]*t,self.pos[1] + self.vel[1]*t

        # vacia la lista de fuerzas en cada iteracion
        self.listaFuerzas = []

    def dibuja(self, color):
        pygame.draw.circle(self.pantalla, self.color, [int(self.pos[0]), int(self.pos[1])], self.radio)
        # print(self.pos)

    def getRadio(self):
        return self.radio

    def getPos(self):
        return self.pos

    def getVel(self):
        return self.vel

    def frena(self):
        self.acel=0, 0
        self.vel=0, 0

    def sumaVelocidad(self, velocidad):
        self.vel=self.vel[0]+velocidad[0], self.vel[1]+velocidad[1]

    def setNormal(self, normal):
        self.normal=normal
        # print(normal)

    # def setSuperposicion(self, superposicion):
    #     self.superposicion = superposicion

    def setFuerza(self,normal,superposicion):
        if superposicion<0:
            superposicion = superposicion * -1
        fuerzaElasica = self.k * superposicion * 0.9
        self.addFuerza([fuerzaElasica * normal[0], fuerzaElasica * normal[1]])

    def addFuerza(self, fuerza):
        self.listaFuerzas.append(fuerza)

    def getFuerza(self):
        suma = 0, 0
        # print(self.listaFuerzas)
        for fuerza in self.listaFuerzas:
            suma = suma[0]+fuerza[0], suma[1]+fuerza[1]
        return suma
