import pygame
from pygame.locals import *
import sys

dim=640,480

def main():
    pygame.init()
    ventana= pygame.display.set_mode(dim)
    pygame.display.set_caption("Escala de grises")


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
if __name__ == "__main__":
    main()
