import pygame
import random
import time
pygame.font.init()

WIDTH,HEIGHT=900,550
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dodge It")
BG=pygame.transform.scale(pygame.image.load("img.png"),(WIDTH,HEIGHT))
OBJECT_HEIGHT=60
OBJECT_WIDTH=40
C=HEIGHT-OBJECT_HEIGHT
OBJECT_VEL=6
Font=pygame.font.SysFont("Times New Roman",35)

def back(object,elapsed_time):
    WIN.blit(BG,(0,0))
    time_txt=Font.render(f"Time:{round(elapsed_time)}s",1,"green")
    WIN.blit(time_txt,(10,0))
    pygame.draw.rect(WIN,"orange",object)
    pygame.display.update()

def main():
    r=True
    object=pygame.Rect(450,C,OBJECT_WIDTH,OBJECT_HEIGHT)
    c=pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0
    while r:
        c.tick(60)
        elapsed_time=time.time()-start_time
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                r=False
                break

        k=pygame.key.get_pressed()
        if k[pygame.K_LEFT] and object.x-OBJECT_VEL>=0:
            object.x-=OBJECT_VEL
        if k[pygame.K_RIGHT] and object.x+OBJECT_VEL+object.width<=WIDTH:
            object.x+=OBJECT_VEL
        back(object,elapsed_time)
    pygame.quit()

if __name__=="__main__":
    main()