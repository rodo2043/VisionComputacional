from time import *
import sys
import Tkinter
from PIL import Image, ImageTk
import random
import math
from math import *

def ventana_bordes(foto4,ancho,alto):# creacion de  ventana de grises                                                                     
    x=0#Cordenadas de posicion de la ventana                                                                                              
    y=0
    ventana_bordes= Tkinter.Tk()#Creacion de ventana                                                                                         
    ventana_bordes.title("Deteccion de bordes")#Titulo de ventana                                                                             
    ventana_bordes.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicion                                                              
    tkimage=ImageTk.PhotoImage(foto4)#Se convierte la imagen en un objeto tk                                                                 
    Tkinter.Label(ventana_bordes,image=tkimage).pack()#Colocar imagen en ventana                                                              
    ventana_bordes.mainloop()


def ventana_grises(foto,ancho,alto):# creacion de  ventana de grises
    x=0#Cordenadas de posicion de la ventana
    y=0
    ventana_gris= Tkinter.Tk()#Creacion de ventana
    ventana_gris.title("Escala de grises")#Titulo de ventana
    ventana_gris.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicion
    tkimage=ImageTk.PhotoImage(foto)#Se convierte la imagen en un objeto tk
    Tkinter.Label(ventana_gris,image=tkimage).pack()#Colocar imagen en ventana
    ventana_gris.mainloop()

def ventana_filtro(foto3,ancho,alto):# creacion de  ventana de grises                                                                          
    x=0#Cordenadas de posicion de la ventana                                                                                              
    y=0
    ventana_filtro= Tkinter.Tk()#Creacion de ventana                                                                                         
    ventana_filtro.title("Filtro")#Titulo de ventana                                                                               
    ventana_filtro.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicion                                                              
    tkimage=ImageTk.PhotoImage(foto3)#Se convierte la imagen en un objeto tk                                                                
    Tkinter.Label(ventana_filtro,image=tkimage).pack()#Colocar imagen en ventana                                                            
    ventana_filtro.mainloop()



def convolucion(foto4,ancho,alto):
    t_in=time()
    Gx=([-1,0,1],[-2,0,2],[-1,0,1])#Formulas Convolucion
    Gy=([1,2,1],[0,0,0],[-1,-2,-1])
    pixeles=foto4.load()
    for i in range(ancho):
        for j in range(alto):
            sumx=0
            sumy=0
            for x in range(len(Gx[0])):
                for y in range(len(Gy[0])):
                    try:
                        sumx +=(pixeles[x+i,y+j][0]*Gx[x][y])
                        sumy +=(pixeles[x+i,y+j][0]*Gy[x][y])
                    except:
                        pass
            Gradiente_Horizontal=pow(sumx,2)#Formulas para obtener el gradiente
            Gradiente_Vertical=pow(sumy,2)
            Magnitud=int(math.sqrt(Gradiente_Horizontal+Gradiente_Vertical))
            #direccion=int(atan(Gradiente_Vertical/Gradiente_Horizontal))
            #pixeles[i,j]=(direccion,direccion,direccion)
            pixeles[i,j]=(Magnitud,Magnitud,Magnitud)
    foto4.save('bordes.jpg')
    t_fi=time()
    tot=t_fi-t_in
    print "Tiempo bordes:"+str(tot)+"segundos"
    ventana_bordes(foto4,ancho,alto)
                                    
def filtro(foto3,ancho,alto):#Funcion para realiza el filtrado
    t_in=time()
    pixeles=foto3.load() #Cargar imagen                                                        
    for i in range(ancho):#Se recogrre la imagen
        for j in range(alto):
            con=0#Contador
            promedio=0
            (r,g,b)=foto3.getpixel((i,j))
            try:
                if(pixeles[i+1,j]):#Vecinos derecho
                    promedio+=pixeles[i+1,j][0]
                    con+=1
            except:
                pass
            try:
                if(pixeles[i-1,j]):#Vecino izq
                    promedio+=pixeles[i-1,j][0]
                    con+=1
            except:
                pass
            try:
                if(pixeles[i,j+1]):#Vecino arriba
                    promedio+=pixeles[i,j+1][0]
                    con+=1
            except:
                pass
            try:
                if(pixeles[i,j-1]):#Vecino abajo
                    promedio+=pixeles[i,j-1][0]
                    con+=1
            except:
                pass
            Total=promedio/con#Promedio entre vecinos disponibles
            pixeles[i,j]=(Total,Total,Total)
    foto3.save('Filtro.jpg')
    t_fi=time()
    tot=t_fi-t_in
    print "Tiempo de filtro:"+str(tot)+"segundos"
    ventana_filtro(foto3,ancho,alto)
    
def umbral(foto2,ancho,alto):#Funcion para generar la imagen umbral
    minimo=random.randint(1,100)#valores para usar en el umbral               
    maximo=random.randint(101,200)
    print "Valor minimo: "+str(minimo)
    print "Valor maximo: "+str(maximo)
    pixeles=foto2.load()#cargar la imagen
    for i in range(ancho):#Se recorre los pixeles de la imagen
        for a in range(alto):
            (r,g,b)=foto2.getpixel((i,a))
            promedio=int((r+g+b)/3)#Obtenemos el promedio de cada pixel
            if promedio <minimo: #Se hace la comparacion con los valores 
                promedio=0
            if promedio >=maximo:
                promedio=255
            pixeles[i,a]=(promedio,promedio,promedio)#Se sustituye el valor de rgb segun sea
    foto2.save('umbral.jpg')#Guardar imagen
    ventana_umbral(foto2,ancho,alto)


def ventana_umbral(foto2,ancho,alto):#creacion de ventana umbral igual que la de gris
    x=0
    y=0
    ventana_umb= Tkinter.Tk()
    ventana_umb.title("Umbral")
    ventana_umb.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))
    tkimage=ImageTk.PhotoImage(foto2)
    Tkinter.Label(ventana_umb,image=tkimage).pack()
    ventana_umb.mainloop()

def escala(foto,ancho,alto):#Creacion de imagen con escala de grises
    pixeles=foto.load()#Proceso igual que el del umbral pero sin las comparaciones
    for i in range(ancho):
        for a in range(alto):
            (r,g,b)=foto.getpixel((i,a))
            promedio=int((r+g+b)/3)
            pixeles[i,a]=(promedio,promedio,promedio)
    foto.save('escalada.jpg')
    ventana_grises(foto,ancho,alto)
   
def main():
    img= str(raw_input('Nombre de imagen: '))#Pedir imagen
    foto=Image.open(img)#Abrir la imagen
    foto2=Image.open(img)#Se almacena en otra variable la misma imagen para usar en umbral
    ancho,alto=foto.size
    escala(foto,ancho,alto)
    umbral(foto2,ancho,alto)
    foto3=Image.open('escalada.jpg')
    filtro(foto3,ancho,alto)
    foto4=Image.open('escalada.jpg')
    convolucion(foto4,ancho,alto)
                                    
main()
