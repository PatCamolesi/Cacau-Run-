#Inicialização biblioteca pygame
import pygame
from random import randint
pygame.init()

#Declaração das variáveis globais
#Posição gatinho_malhado
x = 550
y = 100

#Posição cachorros 1, 2 e 3
pos_x = 280
pos_y = 800

pos_x1 = 570
pos_y1 = 1500

pos_x2 = 840
pos_y2 = 800

#Definição da velocidade do movimento em x do gatinho_malhado
velocidade = 20

#Definição da velocidade inicial do movimento em y dos cachorros 1, 2 e 3
velocidade_cachorro = 8

#Definição dos valores iniciais do marcador de tempo
timer = 0
tempo_segundos = 0

#Carregamento das artes do jogo
fundo = pygame.image.load('Fundo.png')
gatinho = pygame.image.load('gatinho_menor.png')
cachorro1 = pygame.image.load('cachorro_bravo_menor.png')
cachorro2 = pygame.image.load('cachorro_bravo_menor.png')
cachorro3 = pygame.image.load('cachorro_bravo_menor.png')

#Configurações da arte do marcador de tempo
font = pygame.font.SysFont('arial black',30)
text = font.render("Tempo: ", True, (255,255,255),(0,0,0))
pos_texto = text.get_rect()
pos_texto.center = 65,50

#Definição do tamanho da janela, nome do jogo e demais configurações
janela = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Cacau RUN!")

janela_aberta = True
while janela_aberta:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

#Movimento em x do gatinho_malhado e delimitação dos limites à esquerda e à direita
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x<= 800:
        x += velocidade
    if comandos[pygame.K_LEFT] and x>= 280:
        x -= velocidade

#Detecta a colisão à direita:
    if((x + 100 > pos_x2) and (y + 140 > pos_y2)):
        y = 1400

#Detecta a colisão à esquerda:
    if ((x - 100 < pos_x) and (y + 140 > pos_y)):
        y = 1400

#Detecta a colisão no centro:
    if (((x + 50 > pos_x1 < 0) and (y + 140 > pos_y1)) or ((x - 50 < pos_x1 > 0) and (y + 140 > pos_y1))):
        y = 1400

#Movimentação referente à posição randômica dos cachorros 1, 2 e 3
    if(pos_y<=-80) :
        pos_y = randint(800,1300)

    if(pos_y1<= -80):
        pos_y1 = randint(1800,3000)

    if(pos_y2<= -80):
        pos_y2 = randint(3500,5000)

#Configuração timer
    if(timer<20):
        timer +=1
    else:
        tempo_segundos +=1
        text = font.render("Tempo: " + str(tempo_segundos), True, (255, 255, 255), (0, 0, 0))
        timer = 0

#Atualização velocidade de movimentação em y dos cachorros (obstáculos)
    pos_y -= velocidade_cachorro+8
    pos_y1 -= velocidade_cachorro
    pos_y2 -= velocidade_cachorro+1

#Exibição na tela do jogo dos objetos abaixo
    janela.blit(fundo,(0,0))
    janela.blit(gatinho,(x,y))
    janela.blit(cachorro1,(pos_x,pos_y))
    janela.blit(cachorro2,(pos_x1,pos_y1))
    janela.blit(cachorro3,(pos_x2,pos_y2))
    janela.blit(text,pos_texto)

    pygame.display.update()

pygame.quit()

