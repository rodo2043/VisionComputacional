from PIL import Image,ImageDraw
from subprocess import call

def horizontal_histogram(foto,ancho,alto):
    pixeles=foto.load()
    histograma=list()
    fil=open('horizontal.dat','w')
    for x in range(ancho):
        suma=0
        for y in range(alto):
            suma += pixeles[x, y][0]
        fil.write(str(x)+' '+str(suma)+'\n')
        histograma.append(suma)
    fil.close()
    return histograma

def vertical_histogram(foto,ancho,alto):
    pixeles=foto.load()
    histograma=list()
    fil=open('vertical.dat','w')
    for y in range(alto):
        suma=0
        for x in range(ancho):
            suma += pixeles[x, y][0]
        fil.write(str(y)+' '+str(suma)+'\n')
        histograma.append(suma)
    fil.close()
    return histograma

def minimos(histograma):
    mini=list()
    for i in range(len(histograma)):
        try:
            if(histograma[i-1] > histograma[i] and histograma[i+1] > histograma[i]): mini.append(i)
        except:
            pass
    mini.sort()
    return mini

def grafica():
    call(['gnuplot','grafica.gnu'])

def cruzes(hor,ver,foto,ancho,alto):
    draw=ImageDraw.Draw(foto)
    for x in hor:
        draw.line((x, 0, x,ancho), fill=(0,0,255))
    for y in ver:
        draw.line((0,y,alto,y),fill=(255,0,255))
    foto.save("prueb.jpg")
    

def deteccion(foto,ancho,alto):
    foto=escala(foto,ancho,alto)
    foto=filtro(foto,ancho,alto)
    hori=horizontal_histogram(foto,ancho,alto)
    vert=vertical_histogram(foto,ancho,alto)
    horizontal=minimos(hori)
    vertical=minimos(vert)
    cruzes(horizontal,vertical,foto,ancho,alto)
    grafica()
    #foto.save("prueb.jpg")


def escala(foto,ancho,alto):#Creacion de imagen con escala de grises
    pixeles=foto.load()
    for i in range(ancho):
        for a in range(alto):
            (r,g,b)=foto.getpixel((i,a))
            promedio=int((r+g+b)/3)
            pixeles[i,a]=(promedio,promedio,promedio)
    return foto

def filtro(foto,ancho,alto):#Funcion para realiza el filtrado
   # t_in=time()
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
   # t_fi=time()
   # tot=t_fi-t_in
   # print "Tiempo de filtro:"+str(tot)+"segundos"
    return foto

    
def main():
    img=str(raw_input('Nombre de imagen: '))
    foto=Image.open(img)
    ancho,alto=foto.size
    deteccion(foto,ancho,alto)
main()
