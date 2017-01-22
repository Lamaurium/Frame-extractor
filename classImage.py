#!usr/opt/lib
#!encoding: utf-8
import fonction
import cv2
import math
import numpy as np
import variable

class Image():

    def __init__(self, nom, image):
        self.nom = nom
        self.image = image
        self.image_out = image.copy()
        self.pos = []
        self.list_pos = []
        self.filles = []
        self.manip = False
        self.active = False
        self.color = []

    def click(self,event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print "Image selectionnee : " + str(self.nom) + " Active : " + str(self.active)

            if self.active == True:
                self.manip = True

            self.activeI()

            if self.manip == True:
                if len(self.pos)==0:
                    self.pos.append((x,y))
                    cv2.circle(self.image, (self.pos[0][0],self.pos[0][1]) , 20,(0, 155, 0), 2)
                else:
                    if fonction.dist2D((self.pos[len(self.pos) - 1][0],self.pos[len(self.pos) - 1][1]),(x,y))>20:
                        self.pos.append((x,y))
                        for i in self.pos:
                            cv2.circle(self.image, i, 20,(0, 155, 0), 2)
                    else:
                        self.list_pos.append(self.pos)
                        self.rect()
                        self.pos = []
                print self.pos



            self.affImage()

    def getNom(self):
        return self.nom

    def desactive(self):
        self.active = False

    def activeI(self):
        for i in variable.list_image:
            i.active = False
        self.active = True
        for i in variable.list_image:
            print i.active

    def colorInfo(self):
        couleur = ('r','g','b')
        print "aze"
        for j in self.filles:
            print "aze"
            tmp = []
            for i,col in enumerate(couleur):
                hist = cv2.calcHist([j[0]],[i],None,[256],[0,256])
                tmp.append((col, hist))
            self.color.append(tmp)
            tmp = []
        print self.color

    def colorInfoLoc(self, val):
        couleur = ('r','g','b')
        tmp = []
        for i,col in enumerate(couleur):
            hist = cv2.calcHist([val[0]],[i],None,[256],[0,256])
            tmp.append((col, hist))
        return tmp

    def affImage(self):
        cv2.imshow(self.nom, self.image)
        cv2.setMouseCallback(self.nom, self.click)

    def process(self):
        for i in range(0,len(self.list_pos)):
            self.filles.append(self.extract(self.list_pos[i],i))


    def extract(self, position, nom):
#        mask = np.zeros(self.image.shape, dtype=np.uint8)
#        coins = np.array([position], dtype=np.int32)
#        channel_count = self.image.shape[2]
#        ignore_mask_color = (255,)*channel_count
#        cv2.fillPoly(mask, coins, ignore_mask_color)
#        masked_image = cv2.bitwise_and(self.image, mask)

        top, bot, gauche, droite = 10000, 0, 10000, 0
        for i in position:
            if gauche > i[0]:
                gauche = i[0]
            if droite < i[0]:
                droite = i[0]
            if top > i[1]:
                top = i[1]
            if bot < i[1]:
                bot = i[1]

        image_out = self.image_out[top:bot,gauche:droite]
        cv2.imshow(str(nom), image_out)
        return (image_out, str(nom))


    def exportData(self):
        print "<images classe='mere' nom='" + str(self.nom) + "'>"
        for i in self.filles:
            print "\t<image classe='fille' nom='" + str(i[1]) + "'>"
            print "\t\t<taille>" + str(i[0].shape) + "</taille>"
            list_val = self.colorInfoLoc(i)
            for j in list_val:
                print "<couleur col='" + str(j[0]) + "'>" + str(j[1]) + "</couleur>"
            print "\t</image>"

        print "</images>"

    def rect(self):
        top, bot, gauche, droite = 10000, 0, 10000, 0
        for i in self.pos:
            if gauche > i[0]:
                gauche = i[0]
            if droite < i[0]:
                droite = i[0]
            if top > i[1]:
                top = i[1]
            if bot < i[1]:
                bot = i[1]

        cv2.rectangle(self.image, (gauche, top), (droite, bot), (0, 155, 0), 2)
