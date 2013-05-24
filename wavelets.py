import pywt
from PIL import Image
import numpy
import os
import Gnuplot
from time import *

def grises(foto,ancho,alto):#Escala de grises
    pixeles=foto.load()
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)=foto.getpixel((i,j))
            promedio=int((r+g+b)/3)
            pixeles[i,j]=(promedio,promedio,promedio)
    return foto

def resize(foto):#Cambiar tamano de foto
    size=(200,200)
    foto.thumbnail(size,Image.ANTIALIAS)
    return foto

def matriz(foto):#Generar array
    ancho,alto=foto.size
    pixeles=foto.load()
    matrix=numpy.empty((ancho,alto))
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)=foto.getpixel((i,j))
            matrix[i,j]=r
    return matrix
    
def coeficientes(matrix):#Obtener los coefficientes 2D
    coeffs=pywt.dwt2(matrix,'haar')
    cA,(cH,cV,cD)=coeffs#cA=approximacion,cH=Detalle horizontal,cV=Detalle vertical,cD=Detalle diagonal
    return (cA,cH,cV,cD),coeffs

def binario(mat,c,to,ti):#Filtro
    ancho=len(mat)
    alto=len(mat[0])
    nuevo=0
    foto=Image.new('RGB',(ancho,alto))#Crear nueva imagen para almacenar
    pixeles=foto.load()
    for i in range(ancho):
        for j in range(alto):
            if mat[i,j]<0:#Si coefficiente es negativo toma valor de 0
                nuevo=0
            elif mat[i,j]>255:#Si coefficiente es mayor de 255 toma valor de 255
                nuevo=255
            else:
                nuevo=int(mat[i,j])#Si existe otro caso queda con el mismo valor
            pixeles[i,j]=(nuevo,nuevo,nuevo)
    foto.save('coefficiente'+str(c)+'.png')#Genera fotos nuevas
    tf=time()
    tt=tf-ti
    pruebas(c,foto,to,tt)

def pruebas(i,foto,to,tt):
    cont=i
    f=os.stat('coefficiente'+str(cont)+'.png')
    tamano=f.st_size
    porcentaje=(tamano*100)/float(to)
    if cont==0:
        print "-------------------------------------------"
        print "Coefficiente utilizado:cA(Coefficiente de Aproximacion)"
        print "Tamano Imagen original:"+str(to)+"bytes"
        print "Tamano con compression:"+str(tamano)+"bytes"
        print "Porcentaje de compression:"+str(100-porcentaje)+"%"
        print "Tiempo de compression: "+str(tt)+"segundos"
        print "-------------------------------------------"
    if cont==1:
        print "Coefficiente utilizado:cH(Detalle Horizontal)"
        print "Tamano Imagen original:"+str(to)+"bytes"
        print "Tamano con compression:"+str(tamano)+"bytes"
        print "Porcentaje de compression:"+str(100-porcentaje)+"%"
        print "Tiempo de compression: "+str(tt)+"segundos"
        print "-------------------------------------------"
    if cont==2:
        print "Coefficiente utilizado:cV(Detalle Vertical)"
        print "Tamano Imagen original:"+str(to)+"bytes"
        print "Tamano con compression:"+str(tamano)+"bytes"
        print "Porcentaje de compression:"+str(100-porcentaje)+"%"
        print "Tiempo de compression: "+str(tt)+"segundos"
        print "-------------------------------------------"
    if cont==3:
        print "Coefficiente utilizado:cD(Detalle Diagonal)"
        print "Tamano Imagen original:"+str(to)+"bytes"
        print "Tamano con compression:"+str(tamano)+"bytes"
        print "Porcentaje de compression:"+str(100-porcentaje)+"%"
        print "Tiempo de compression: "+str(tt)+"segundos"
        print "-------------------------------------------"



def nueva_imagen(coe,to):#Envia coefficientes al filtro(binario)
    for c,i in enumerate(coe):
        ti=time()
        binario(i,c,to,ti)

def inversa(coefficientes,escala):#Funcion para recuperar original
    inv=pywt.idwt2(coefficientes,'haar')#Funcion inversa
    pixeles=escala.load()
    ancho,alto=escala.size
    for i in range(ancho):
        for j in range(alto):
            nuevo=int(inv[i,j])
            pixeles[i,j]=(nuevo,nuevo,nuevo)
    return escala

def main():
    img=str(raw_input('Nombre de imagen: '))#cargar imagen
    foto=Image.open(img)
    ancho,alto=foto.size
    f=os.stat(img)
    tamano_original=f.st_size
    escala=grises(foto,ancho,alto)
    escala.save('grises.jpg')
    nueva=resize(escala)
    matrix=matriz(nueva)
    coe,coeff=coeficientes(matrix)
    nueva_imagen(coe,tamano_original)
    foto=inversa(coeff,escala)
    foto.save('Inversa.jpg')
main()
