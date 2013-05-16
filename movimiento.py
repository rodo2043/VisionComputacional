import cv
from PIL import Image,ImageFont,ImageDraw
import math


def filtro(foto,ancho,alto):#Funcion para realiza el filtrado
    #t_in=time()
    pixeles=foto.load() #Cargar imagen                                                        
    for i in range(ancho):#Se recogrre la imagen
        for j in range(alto):
            con=0#Contador
            promedio=0
            (r,g,b)=foto.getpixel((i,j))
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
    #t_fi=time()
    #tot=t_fi-t_in
    #print "Tiempo de filtro:"+str(tot)+"segundos"
    return foto

def convolucion(foto,ancho,alto):
    gx=[]
    gy=[]
    magnitud=[]
    Gx=([-1,0,1],[-2,0,2],[-1,0,1])#Formulas Convolucion
    Gy=([1,2,1],[0,0,0],[-1,-2,-1])
    pixeles=foto.load()
    for i in range(alto):
        gx.append([])
        gy.append([])
        for j in range(ancho):
            sumx=0
            sumy=0
            for x in range(len(Gx[0])):
                for y in range(len(Gy[0])):
                    try:
                        sumx +=(pixeles[j+y,i+x][0]*Gx[x][y])
                        sumy +=(pixeles[j+y,i+x][0]*Gy[x][y])
                    except:
                        pass
                    Gradiente_Horizontal=pow(sumx,2)#Formulas para obtener el gradiente
                    Gradiente_Vertical=pow(sumy,2)
                    Magnitud=int(math.sqrt(Gradiente_Horizontal+Gradiente_Vertical))
                    gx[i].append(sumx)
                    gy[i].append(sumy)
                    pixeles[j,i]=(Magnitud,Magnitud,Magnitud)
    return foto

def binarizacion(foto,ancho,alto):
    x=0
    pixeles=foto.load()
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)=foto.getpixel((i,j))
            promedio=int((r+g+b)/3)
            if promedio > x:
                pixeles[i,j]=(255,255,255)
            else:
                pixeles[i,j]=(0,0,0)
    return foto

def escala(foto,ancho,alto):#Creacion de imagen con escala de grises
    pixeles=foto.load()#Proceso igual que el del umbral pero sin las comparaciones
    for i in range(ancho):
        for a in range(alto):
            (r,g,b)=foto.getpixel((i,a))
            promedio=int((r+g+b)/3)
            pixeles[i,a]=(promedio,promedio,promedio)
    return foto

def imagen1():
    cam=cv.CaptureFromCAM(0)
    while True:
        im =cv.QueryFrame(cam)
        snapshot = im
        image_size = cv.GetSize(snapshot)
        cv.SaveImage("test.png",im)
        imagen=cv.CreateImage(image_size,cv.IPL_DEPTH_8U,3)
        
        break

    

def imagen2():
    cam=cv.CaptureFromCAM(0)
    while True:
        im =cv.QueryFrame(cam)
        snapshot = im
        image_size = cv.GetSize(snapshot)
        cv.SaveImage("test2.png",im)
        imagen=cv.CreateImage(image_size,cv.IPL_DEPTH_8U,3)
        
        break

def diferencia():
    foto=Image.open('Binarizacion1.png')
    ancho,alto=foto.size
    foto1=Image.open('Binarizacion2.png')
    ancho1,alto1=foto1.size
    foto2=Image.new("RGB",(ancho1,alto1))
    pixeles=foto.load()
    pixeles2=foto1.load()
    pixeles3=foto2.load()
    for i in range(ancho-1):
        for j in range(alto-1):
            diferen=abs(pixeles[i,j][0]-pixeles2[i,j][0])
            if diferen !=0:
                pixeles3[i,j]=(255,255,255)
            else:
                pixeles3[i,j]=(0,0,0)
    return foto2

def movimiento():
    foto=Image.open('Binarizacion1.png')
    ancho,alto=foto.size
    foto1=Image.open('Diferencia.png')
    ancho1,alto1=foto1.size
    foto2=Image.new("RGB",(ancho1,alto1))
    pixeles=foto.load()
    pixeles2=foto1.load()
    pixeles3=foto2.load()
    for i in range(ancho):
        for j in range(alto):
            diferen=abs(pixeles[i,j][0]-pixeles2[i,j][0])
            if diferen !=0:
                pixeles3[i,j]=(255,255,255)
            else:
                pixeles3[i,j]=(0,0,0)

    return foto2

def marcar():
    original=Image.open('Binarizacion1.png')
    mov=Image.open('Movimiento.png')
    original2=Image.open('Binarizacion2.png')
    ancho1,alto1=original.size
    ancho2,alto2=mov.size
    ancho3,alto3=original2.size
    pixeles=original.load()
    pixeles2=original2.load()
    pixeles3=mov.load()
    draw = ImageDraw.Draw(original2)
    fuente = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf',20)
    for i in range(alto2):
        for j in range(ancho2):
            (r,g,b)=original.getpixel((j,i))
            (r,g,b)=original2.getpixel((j,i))
            (r,g,b)=mov.getpixel((j,i))
            a=1
            b=0
            ultimo=0
            if pixeles2[j,i][0]==255:
                while a < ancho2:
                    if j+a >= 0 and j+a < ancho1-10 and i+b >= 0 and i+b < alto1-10:
                        if pixeles[j+a,i][0]!=0:
                            ultimo=a
                            pixeles[j+a,i]=(0,0,0)
                            a=ancho2
                            direccion='derecha'
                            break
                    if j-a >= 0 and j-a < ancho1-10 and i+b >= 0 and i+b < alto1-10:
                        if pixeles[j-a,i][0] !=0:
                            ultimo=a
                            pixeles[j-a,i]=(0,0,0)
                            a=ancho2
                            direccion='Izquierda'
                            break
                    a+=1
                if ultimo !=0:
                    x,y=j,i
                    draw.line((j,i,j+ultimo,i),fill=128)
    draw.text((x,y), ' '+direccion+ '', fill=(255,0,0),font=fuente)
    return original2

def main():
    i=0
    ans= str(raw_input('Obtener primera imagen?: '))
    if ans=="si":
        print "Get ready :P"
        imagen1()
        i+=1
    ans= str(raw_input('Obtener segunda imagen?: '))
    if ans=="si":
        print "Get ready :P"
        imagen2()
        i+=1
    if i==2:
        foto1=Image.open('test.png')
        ancho,alto=foto1.size
        escalada=escala(foto1,ancho,alto)
        escalada.save('Escala1.png')
        filtrada=filtro(escalada,ancho,alto)
        filtrada.save('Filatrada1.png')
        convu=convolucion(filtrada,ancho,alto)
        convu.save('Convolucion1.png')
        binaria=binarizacion(convu,ancho,alto)
        binaria.save('Binarizacion1.png')
        foto2=Image.open('test2.png')
        ancho,alto=foto2.size
        escalada=escala(foto2,ancho,alto)
        escalada.save('Escala2.png')
        filtrada=filtro(escalada,ancho,alto)
        filtrada.save('Filatrada2.png')
        convu=convolucion(filtrada,ancho,alto)
        convu.save('Convolucion2.png')
        binaria=binarizacion(convu,ancho,alto)
        binaria.save('Binarizacion2.png')
        #foto1=Image.open('Binarizacion1.png')
        dif=diferencia()
        dif.save('Diferencia.png')
        mov=movimiento()
        mov.save('Movimiento.png')
        mar=marcar()
        mar.save('Marcado.png')
    else:
        print "No se puede continuar ya que no se genero alguna de las 2 fotos"
    
    
main()
