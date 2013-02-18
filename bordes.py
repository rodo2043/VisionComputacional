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
    ventana_bordes.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicio
    tkimage=ImageTk.PhotoImage(foto4)#Se convierte la imagen en un objeto t
    Tkinter.Label(ventana_bordes,image=tkimage).pack()#Colocar imagen en venta
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
    ventana_filtro.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicio
    tkimage=ImageTk.PhotoImage(foto3)#Se convierte la imagen en un objeto tk 
    Tkinter.Label(ventana_filtro,image=tkimage).pack()#Colocar imagen en venta
    ventana_filtro.mainloop()

def ventana_salpi(foto5,ancho,alto):# creacion de  ventana de grises                                                       
    x=0#Cordenadas de posicion de la ventana                                                                                     
    y=0
    ventana_salpi= Tkinter.Tk()#Creacion de ventana                                                                                      
    ventana_salpi.title("Aplicacion Sal Pimienta")#Titulo de ventana                                                                      
    ventana_salpi.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicio                                                             
    tkimage=ImageTk.PhotoImage(foto5)#Se convierte la imagen en un objeto tk                                                                
    Tkinter.Label(ventana_salpi,image=tkimage).pack()#Colocar imagen en venta                                                              
    ventana_salpi.mainloop()

def ventana_primerfiltrado(foto5,ancho,alto):# creacion de  ventana de grises                                                               
    x=0#Cordenadas de posicion de la ventana                                                                                              
    y=0
    ventana_primerfiltrado= Tkinter.Tk()#Creacion de ventana                                                                                
    ventana_primerfiltrado.title("Primer filtro de removido")#Titulo de ventana                                                              
    ventana_primerfiltrado.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicio                                                       
    tkimage=ImageTk.PhotoImage(foto5)#Se convierte la imagen en un objeto tk                                                                
    Tkinter.Label(ventana_primerfiltrado,image=tkimage).pack()#Colocar imagen en venta                                                       
    ventana_primerfiltrado.mainloop()

def ventana_segundofiltrado(foto5,ancho,alto):# creacion de  ventana de grises                                                               
    x=0#Cordenadas de posicion de la ventana                                                                                              
    y=0
    ventana_segundofiltrado= Tkinter.Tk()#Creacion de ventana                                                                                
    ventana_segundofiltrado.title("Segundo filtro remover todo")#Titulo de ventana                                                           
    ventana_segundofiltrado.geometry("%dx%d+%d+%d" % (ancho,alto,x,y))#Tamano y posicio                                                      
    tkimage=ImageTk.PhotoImage(foto5)#Se convierte la imagen en un objeto tk                                                                
    Tkinter.Label(ventana_segundofiltrado,image=tkimage).pack()#Colocar imagen en venta                                                      
    ventana_segundofiltrado.mainloop()


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
                                    
def sal_pimienta(foto5,ancho,alto):
    t_in=time()
    pixeles=foto5.load()
    intensidad=float(raw_input('Ingrese la intensidad 1 siendo lo mas alto:'))#Declaramos un valor intensidad 1 recorre la imagen completa
    con=0
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)=foto5.getpixel((i,j))#recorremos la imagen
            if(random.random()<intensidad):
                try:
                    
                    x=random.randint(0,1000)#Generamos un valor random para sumar al pixel actual que es donde se agregara ruido
                # print x
                    if(x%2):#Si el numero generado es modulo de 2 el pixel pintado sera blanco
                        pixeles[i+x,j+x]=(255,255,255)
                        con+=1
                    else:
                        pixeles[i+x,j+x]=(0,0,0)#Si no es modulo se pinta negro
                        con+=1
                except:
                    pass
    t_fi=time()
    total=t_fi-t_in
    foto5.save('ruido.jpg')
    print "Se a agregado ruido a "+str(con)+" pixeles"
    print "El tiempo de ejecuccion al agregar ruido es de "+str(total)+" Segundos"
    ventana_salpi(foto5,ancho,alto)#Crear ventana de sal pimienta
    eliminar_salp(foto5,ancho,alto)#llamado a funcion para eliminar sal pimienta
    

def eliminar_salp(foto5,ancho,alto):
    pixeles=foto5.load()
    t_in=time()
    con=0
    con2=0
    for i in range(ancho):
        for j in range (alto):#Recorrer imagen
            promedio=0
            con2=0
            (r,g,b)=foto5.getpixel((i,j))
            if(pixeles[i,j]==(255,255,255) or pixeles[i,j]==(0,0,0)):#Si el pixel actual es blanco o negro
                con+=1
                try:
                    if (pixeles[i-1,j]):#Revisar vecino izq
                        if (pixeles[i-1,j]==(255,255,255) or pixeles[i-1,j]==(0,0,0)):# Si su vecino izq es negro o blanco no tomar en cuenta
                            promedio+=0
                            
                        else:
                            promedio+=pixeles[i-1,j][0]#Si es de otro color sumar a promedio
                            con2+=1
                except:
                    pass
                try:
                    if (pixeles[i+1,j]):#revisar vecino der
                        if (pixeles[i+1,j]==(255,255,255) or pixeles[i+1,j]==(0,0,0)):#Si el vecino derecho es blanco o negro no tomar
                            promedio+=0
                        else:
                            promedio+=pixeles[i+1,j][0]#Si es de otro color sumar a promedio
                            con2+=1
                except:
                    pass
                try:
                    if (pixeles[i,j-1]):#Revisar vecino abajo
                        if (pixeles[i,j-1]==(255,255,255) or pixeles[i,j-1]==(0,0,0)):#Lo mismo vecino de abajo
                            promedio+=0
                        else:
                            promedio+=pixeles[i,j-1][0]
                            con2+=1
                except:
                    pass
                try:
                    if (pixeles[i,j+1]):#Revisar vecino de arriba
                        if (pixeles[i,j+1]==(255,255,255) or pixeles[i,j+1]==(0,0,0)):#Lo mismo vecino de arriba
                            promedio+=0
                        else:
                            promedio+=pixeles[i,j+1][0]
                            con2+=1
                except:
                    pass
                try:
                    Total=promedio/con2
                    pixeles[i,j]=(Total,Total,Total)
                except:
                    pass
                #print promedio
                #print con2

    foto5.save('sinruido.jpg')
    t_fi=time()
    tot=t_fi-t_in
    print "Tiempo del primerfiltrado:"+str(tot)+"segundos"
    ventana_primerfiltrado(foto5,ancho,alto)
    segundofiltro(foto5,ancho,alto)
    print "Se han encontrado "+str(con)+" pixeles con ruido"

def segundofiltro(foto5,ancho,alto):#Funcion que realiza el mismo proceso que el filtro pero para la foto obtenida de la eliminacion de salpi
    t_in=time()
    pixeles=foto5.load() #Cargar imagen                                                        
    for i in range(ancho):#Se recogrre la imagen
        for j in range(alto):
            con=0#Contador
            promedio=0
            (r,g,b)=foto5.getpixel((i,j))
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
    foto5.save('SegundoFiltroSalPimienta.jpg')
    t_fi=time()
    tot=t_fi-t_in
    print "Tiempo del segundofiltrado:"+str(tot)+"segundos"
    ventana_segundofiltrado(foto5,ancho,alto)
                
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

def binarizacion(foto6,ancho,alto):
    x=random.randint(50,100)
    print "Valor maximo binarizacion:"+str(x)
    pixeles=foto6.load()
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)=foto6.getpixel((i,j))
            promedio=int((r+g+b)/3)
            if promedio < x:
                pixeles[i,j]=(0,0,0)
            else:
                pixeles[i,j]=(255,255,255)
    foto6.save('binarizacion.jpg')
    formas(foto6,ancho,alto)

def formas(foto6,ancho,alto):
    pixeles=foto6.load()#Cargar imagen
    for i in range(ancho):#Recorrer imagen
        for j in range (alto):
            if pixeles[i,j]==(0,0,0):#Si el pixel actual es negro
                col1=random.randint(0,255)
                col2=random.randint(0,255)#Se genera un color random
                col3=random.randint(0,255)
                r,g,b=(col1,col2,col3)
                bfs(foto6,(i,j),(r,g,b),ancho,alto)#Se llama al bfs

def bfs(foto6,actual,color,ancho,alto):
    pixeles=foto6.load()
    cola=[]#Se crea la cola
    cola.append(actual)#Se agrega el valor actual a la cola
    partida=pixeles[actual]#punto de partida
    while len(cola)>0:#Mientras existan valores en la cola hacer...
        (x,y)=cola.pop(0)#Removemos el valor de la cola
        actual=pixeles[x,y]#actual toma el valor de la cola
        if actual==partida or actual ==color:#Si el pixel actual es igual al punto de partida o color 
            
            try:
                if (pixeles[x-1,y]):#Revisar vecino izq
                    if (pixeles[x-1,y]==partida):#Si rgb de vecino izq es igual a punto de partida
                        pixeles[x-1,y]=color#Pintar pixel de color
                        cola.append((x-1,y))#Y agregar a cola
            except:
                pass

            try:
                if (pixeles[x+1,y]):#Revisar vecino der                                                
                    if (pixeles[x+1,y]==partida):#Lo mismo vecino der
                        pixeles[x+1,y]=color
                        cola.append((x+1,y))
            except:
                pass
            try:
                if (pixeles[x,y-1]):#Revisar vecino abajo                                              
                    if (pixeles[x,y-1]==partida):#Lo mismo vecino abajo
                        pixeles[x,y-1]=color
                        cola.append((x,y-1))
                                    
            except:
                pass

            try:
                if (pixeles[x,y+1]):#Revisar vecino arriba                                              
                    if (pixeles[x,y+1]==partida):#Lo mismo vecino arriba
                        pixeles[x,y+1]=color
                        cola.append((x,y+1))
            except:
                pass
            
    foto6.save('prueba.jpg')
        
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
    foto5=Image.open(img)
    ancho,alto=foto.size
    escala(foto,ancho,alto)
 #   umbral(foto2,ancho,alto)
    foto3=Image.open('escalada.jpg')
  #  filtro(foto3,ancho,alto)
    foto4=Image.open('escalada.jpg')
    convolucion(foto4,ancho,alto)
   # sal_pimienta(foto5,ancho,alto)
    foto6=Image.open('bordes.jpg')
    binarizacion(foto6,ancho,alto)
main()
