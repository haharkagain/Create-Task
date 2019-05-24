import sys
import pygame
import idlelib
import os
import random

#-------------------- CLASS DECLARATIONS ----------------------#
wallsX = []
wallsY = []

class Thing:

    def __init__(self, posX, posY, orientation):
        self.posX = posX
        self.posY = posY
        self.orientation = orientation
        self.leftEdge = 0 
        self.rightEdge = 0
        self.bottomEdge = 0
        self.topEdge = 0
        self.hitBottom = False
        self.next = False
        self.shape = random.randint(1, 7)
        self.score = 0
        self.cooldown = 10

        colorNumber = random.randint(1, 6)
        if colorNumber == 1:
            self.color = RED
        if colorNumber == 2:
            self.color = DBLUE
        if colorNumber == 3:
            self.color = GREEN
        if colorNumber == 4:
            self.color = LBLUE
        if colorNumber == 5:
            self.color = PURPLE
        if colorNumber == 6: 
            self.color = YELLOW
    
    def move(self):
        if self.leftEdge < 0:
            self.posX += 35
        if self.rightEdge > edgeX - 35:
            self.posX -= 35
        if self.bottomEdge > edgeY - 35:
            self.posY -= 35            

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if ((self.leftEdge > 0) and (self.cooldown >= 10)):
                self.posX -= 35
                self.cooldown = 0
        if key[pygame.K_RIGHT]:
            if ((self.rightEdge < edgeX - 35) and (self.cooldown >= 10)):
                self.posX += 35
                self.cooldown = 0
        if key[pygame.K_DOWN]:
            if self.bottomEdge < edgeY - 35:
                self.posY += 35
            else:
                self.hitBottom = True
            
    def shapeType(self):
        if self.shape == 1:
            thing.square()
        if self.shape == 2:
            thing.LShape()
        if self.shape == 3:
            thing.reverseLShape()
        if self.shape == 4:
            thing.TShape()
        if self.shape == 5:
            thing.rectangle()
        if self.shape == 6:
            thing.stair()
        if self.shape == 7:
            thing.reverseStair()

    def nextShape(self):
        row = edgeY
        clearUnits = []
        while row > 0:
            for i in range(len(wallsY)):
                if row == wallsY[i]:
                    clearUnits.append(i)
            if len(clearUnits) == 10:
                for i in range(len(clearUnits) - 1, -1, -1 ):
                    del wallsX[clearUnits[i]]
                    del wallsY[clearUnits[i]]
                for i in range(len(wallsY)):
                    if row >= wallsY[i]:
                        wallsY[i] = wallsY[i] + 35
                row = edgeY + 35
                self.score += 10
            for i in range(len(clearUnits)):
                del clearUnits[0]         
            row -= 35
        self.posX = 140
        self.posY = 0
        self.leftEdge = 0 
        self.rightEdge = 0
        self.bottomEdge = 0
        self.topEdge = 0
        self.hitBottom = False
        self.next = False
        self.orientation = 0
        self.shape = random.randint(1, 7)
        
    def colorPicker(self):
        colorNumber = random.randint(1, 6)
        if colorNumber == 1:
            self.color = RED
        if colorNumber == 2:
            self.color = DBLUE
        if colorNumber == 3:
            self.color = GREEN
        if colorNumber == 4:
            self.color = LBLUE
        if colorNumber == 5:
            self.color = PURPLE
        if colorNumber == 6: 
            self.color = YELLOW

    def square(self):
        pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
        pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
        pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
        pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY + 35, 35, 35))

        self.leftEdge = self.posX
        self.rightEdge = self.posX + 35
        self.bottomEdge = self.posY + 35
        self.topEdge = self.posY

        for i in range (len(wallsX)):
            if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                self.hitBottom = True
            if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                self.hitBottom = True
            if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                self.hitBottom = True
            if ((self.posX + 35 == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                self.hitBottom = True 

        if self.hitBottom == True:
            wallsX.append(self.posX)
            wallsY.append(self.posY)

            wallsX.append(self.posX + 35)
            wallsY.append(self.posY)

            wallsX.append(self.posX)
            wallsY.append(self.posY + 35)

            wallsX.append(self.posX + 35)
            wallsY.append(self.posY + 35)

            self.next = True
    
    def LShape(self):

        if self.orientation == 0: # horizontal, peg down left
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 70, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))

            self.leftEdge = self.posX
            self.rightEdge = self.posX + 70
            self.bottomEdge = self.posY + 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 70 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 70)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                self.next = True

        if self.orientation == 1: # vertical, peg bottom right
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 70, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))

            self.leftEdge = self.posX
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY
            self.topEdge = self.posY - 70

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 70 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 70)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                self.next = True

        if self.orientation == 2: # horizontal, peg up right
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 70, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))

            self.leftEdge = self.posX - 70
            self.rightEdge = self.posX
            self.bottomEdge = self.posY
            self.topEdge = self.posY - 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 70 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX - 70)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                self.next = True

        if self.orientation == 3: # vertical, peg up left
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 70, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))

            self.leftEdge = self.posX - 35
            self.rightEdge = self.posX
            self.bottomEdge = self.posY + 70
            self.topEdge = self.posY

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 70 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 70)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                self.next = True

    def TShape(self):
        if self.orientation == 0: # peg up
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))

            self.leftEdge = self.posX - 35
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY
            self.topEdge = self.posY - 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                self.next = True
            
        if self.orientation == 1: # peg right
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))

            self.leftEdge = self.posX
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY + 35
            self.topEdge = self.posY - 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                self.next = True

        if self.orientation == 2: # peg down
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))

            self.leftEdge = self.posX - 35
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY + 35
            self.topEdge = self.posY

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                self.next = True

        if self.orientation == 3: # peg left
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))

            self.leftEdge = self.posX - 35
            self.rightEdge = self.posX
            self.bottomEdge = self.posY + 35
            self.topEdge = self.posY - 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                self.next = True

    def reverseLShape(self):
        if self.orientation == 0: # horizontal peg down right
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 70, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))

            self.leftEdge = self.posX - 70
            self.rightEdge = self.posX
            self.bottomEdge = self.posY + 35
            self.topEdge = self.posY

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 70 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX - 70)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                self.next = True
            
        if self.orientation == 1: # vertical peg down left
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 70, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))

            self.leftEdge = self.posX - 35
            self.rightEdge = self.posX
            self.bottomEdge = self.posY
            self.topEdge = self.posY - 70

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 70 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 70)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                self.next = True

        if self.orientation == 2: # horizontal peg up left
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 70, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))

            self.leftEdge = self.posX
            self.rightEdge = self.posX + 70
            self.bottomEdge = self.posY
            self.topEdge = self.posY - 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 70 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 70)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                self.next = True

        if self.orientation == 3: # vertical peg up right
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 70, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))

            self.leftEdge = self.posX
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY + 70
            self.topEdge = self.posY

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 70 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 70)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                self.next = True

    def rectangle(self):
        if ((self.orientation == 0) or (self.orientation == 2)): # horizontal
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 70, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))

            self.leftEdge = self.posX - 35
            self.rightEdge = self.posX + 70
            self.bottomEdge = self.posY
            self.topEdge = self.posY

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 70 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 70)
                wallsY.append(self.posY)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                self.next = True
            
        if ((self.orientation == 1) or (self.orientation == 3)): # vertical
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 70, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))

            self.leftEdge = self.posX
            self.rightEdge = self.posX 
            self.bottomEdge = self.posY + 70
            self.topEdge = self.posY - 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 70 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 70)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                self.next = True

    def stair(self):
        if ((self.orientation == 0) or (self.orientation == 2)): # horizontal
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY + 35, 35, 35))

            self.leftEdge = self.posX - 35
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY + 35
            self.topEdge = self.posY

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY + 35)

                self.next = True
            
        if ((self.orientation == 1) or (self.orientation == 3)): # vertical
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY - 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY + 35, 35, 35))

            self.leftEdge = self.posX
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY + 35
            self.topEdge = self.posY - 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY - 35)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY + 35)

                self.next = True

    def reverseStair(self):
        if ((self.orientation == 0) or (self.orientation == 2)): # horizontal
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX - 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY + 35, 35, 35))         

            self.leftEdge = self.posX - 35
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY + 35
            self.topEdge = self.posY

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX - 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX - 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY + 35)

                self.next = True
            
        if ((self.orientation == 1) or (self.orientation == 3)): # vertical
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX, self.posY + 35, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY, 35, 35))
            pygame.draw.rect(screen, self.color, (self.posX + 35, self.posY - 35, 35, 35))

            self.leftEdge = self.posX
            self.rightEdge = self.posX + 35
            self.bottomEdge = self.posY + 35
            self.topEdge = self.posY - 35

            for i in range (len(wallsX)):
                if ((self.posX == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX == wallsX[i]) and (self.posY + 35 == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY == wallsY[i] - 35)):
                    self.hitBottom = True
                if ((self.posX + 35 == wallsX[i]) and (self.posY - 35 == wallsY[i] - 35)):
                    self.hitBottom = True 

            if self.hitBottom == True:
                wallsX.append(self.posX)
                wallsY.append(self.posY)

                wallsX.append(self.posX)
                wallsY.append(self.posY + 35)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY)

                wallsX.append(self.posX + 35)
                wallsY.append(self.posY - 35)

                self.next = True

#----------------------------------------------------------------------------------------#


#------DEFINITIONS------#
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
LBLUE = (0, 255, 255)
GREEN = (0, 255, 0)
DBLUE = (0, 0, 255)
RED = (255, 0, 0)
#-----------------------#

#----- INITIATION -----#
edgeX = 350
edgeY = 700

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

size =  (edgeX, edgeY)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
thing = Thing(140, 0, 0)

font = pygame.font.SysFont('Comic Sans MS', 32)
text = font.render('{}'.format(thing.score), False, BLACK)
text2 = font.render('Final Score', False, BLACK)

timer = 0
#---------------------------------------------#

#------------- GLOBAL FUNCTIONS -------------#
def coordinatePlane():
    offset = 35
    for i in range (int(edgeX / offset)):
        current = offset * i
        pygame.draw.line(screen, BLACK, [current, 0], [current, edgeY], 1)
    for i in range (int(edgeY / offset)):
        current = offset * i
        pygame.draw.line(screen, BLACK, [0, current], [edgeX, current], 1)

#---------------------------------------------------------------------------#

#------------- GAME LOOP -----------------------#
done = False
while (not done):   
    for event in (pygame.event.get()):
        if (event.type == pygame.QUIT):
            done = True                         # exit
        elif(event.type == pygame.KEYUP):
            if event.key == pygame.K_UP:
                thing.orientation = (thing.orientation + 1) % 4
    
    screen.fill(WHITE)
    
    coordinatePlane()
    thing.shapeType()
    thing.move()

    if timer == 30:
        thing.posY += 35
        timer = 0  
    else:
        timer += 1
    thing.cooldown += 2

    for i in range (len(wallsX)):
        pygame.draw.rect(screen, BLACK, (wallsX[i], wallsY[i], 35, 35))

    if thing.next == True:
        thing.colorPicker()
        thing.nextShape()
        thing.hitBottom = False
        text = font.render('{}'.format(thing.score), False, BLACK)

    for i in range (len(wallsY)):
        if wallsY[i] == 0:
            done = True
    
    screen.blit(text, (edgeX / 2, 0))
      
    pygame.display.flip()
    clock.tick(60)

#--------------------------------------------------------------------------------------------------------------------------------#

#--------- Ending Screen -------------#
done = False
while (not done):
    for event in (pygame.event.get()):
        if (event.type == pygame.QUIT):
            done = True
    screen.fill(WHITE)
    screen.blit(text2, (100, 250))
    screen.blit(text, (edgeX / 2, 350))
    pygame.display.flip()
    clock.tick(60)

#----------------------------------------# 

pygame.quit()   