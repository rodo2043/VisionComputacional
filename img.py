import sys
import Tkinter
from PIL import Image, ImageTk
import random

def ventana_grises(foto,ancho,alto):# creacion de  ventana de grises
    x=0#Cordenadas de posicion de la ventana
    y=0
    ventana_gris= Tkinter.Tk()#Creacion de ventana
    ventana_gris.title("Escala de grises")#Titulo de ventana
    ventana_gris.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicion
    tkimage=ImageTk.PhotoImage(foto)#Se convierte la imagen en un objeto tk
    Tkinter.Label(ventana_gris,image=tkimage).pack()#Colocar imagen en ventana
    ventana_gris.mainloop()
    

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
            if promedio <= minimo: #Se hace la comparacion con los valores 
                promedio=0
            if promedio >= maximo:
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
main()
