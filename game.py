import pygame
from random import randint #função randomiza valores
pygame.font.init() #Inicializa objeto font
pygame.init #Iniciar aplicação

x = 400
y = 300
pos_x = 300
pos_y = 800
pos_y_a = 800
pos_y_c = 800
velocidade = 30
velocidade_outros = 15

timer = 0
tempo_segundos = 0


fundo = pygame.image.load('FundoGame2.png')
carro1 = pygame.image.load('laranja-removebg-preview.png')
carro2 = pygame.image.load('amarelo-removebg-preview (3).png')
carro3 = pygame.image.load('verde.png')
carro4 = pygame.image.load('zul-removebg-preview.png')

#time
font = pygame.font.SysFont('arial',30) #Objeto fonte
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0)) #Cor da letra e fonte


#Criando janela
janela = pygame.display.set_mode((800,600)) #Tamanho da tela
pygame.display.set_caption("Jogo em Python") #Nome da tela

janela_aberta = True
while janela_aberta:    #Enquanto janela aberta
    pygame.time.delay(50)
    for event in pygame.event.get() :   #Aguarda evento get
        if event.type == pygame.QUIT:   #Se evento get for QUIT
            janela_aberta = False       #Janela vai encerrar

    #Comando de movimentação
    comandos = pygame.key.get_pressed()
    
    #if comandos [pygame.K_UP]: #Seta para cima
        # y -= velocidade #Decrementar
    #if comandos [pygame.K_DOWN]:
       # y += velocidade #Incrementar
    if comandos [pygame.K_LEFT] and x >=85:
        x -= velocidade
    if comandos [pygame.K_RIGHT] and x <= 575:
        x += velocidade
    if(pos_y <= -200):
        pos_y=600
    pos_y -= velocidade_outros

    #colisão direita
    if (x+90 > pos_x and y + 170> pos_y):
       y = 1300

    # if pos_y.colidirect(pos_y_c):
    #    print('Game Over')




    #movimentação carros
    if (pos_y <= -80) :
        pos_y = randint(800,1200)
    if (pos_y_a <= -80):
       pos_y_a = randint(1200,1400)
    if (pos_y_c <= -80):
        pos_y_c = randint(1400,1800)
    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros+6
    pos_y_c -= velocidade_outros+12

    if (timer < 20):
        timer +=1
    else:
        tempo_segundos +=1
        texto = font.render("Tempo: "+str(tempo_segundos),True,(255,255,255),(0,0,0))
        timer = 0

    #janela.fill((0,0,0))
    #pygame.draw.circle(janela,(0, 255, 200),(x,y), 50) 
                       #janela, cor, local, tamanho circulo
                    
   
    
    janela.blit(fundo,(0,0))
    janela.blit(carro1,(x,y-150))
    janela.blit(carro2,(pos_x -210,pos_y_a))
    janela.blit(carro3,(pos_x + 250,pos_y_c))
    janela.blit(carro4,(pos_x -70,pos_y))
    janela.blit(texto,(2,30))

    pygame.display.update()






pygame.QUIT() #Encerrar o game