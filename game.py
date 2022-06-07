import pygame
pygame.init #Iniciar aplicação

x = 400
y = 300
pos_x = 300
pos_y = 200
velocidade = 20
velocidade_outros = 15
fundo = pygame.image.load('FundoGame2.png')
carro1 = pygame.image.load('laranja-removebg-preview.png')
carro2 = pygame.image.load('amarelo-removebg-preview (3).png')
carro3 = pygame.image.load('da-removebg-preview (3).png')
carro4 = pygame.image.load('zul-removebg-preview.png')

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
    
    if comandos [pygame.K_UP]: #Seta para cima
        y -= velocidade #Decrementar
    if comandos [pygame.K_DOWN]:
        y += velocidade #Incrementar
    if comandos [pygame.K_LEFT]:
        x -= velocidade
    if comandos [pygame.K_RIGHT]:
        x += velocidade
    if(pos_y <= -200):
        pos_y=600
    pos_y -= velocidade_outros



    #janela.fill((0,0,0))
    #pygame.draw.circle(janela,(0, 255, 200),(x,y), 50) 
                       #janela, cor, local, tamanho circulo
                    
   
    
    janela.blit(fundo,(0,0))
    janela.blit(carro1,(x,y))
    janela.blit(carro2,(pos_x -210,pos_y))
    janela.blit(carro3,(pos_x + 250,pos_y))
    janela.blit(carro4,(pos_x -70,pos_y))

    pygame.display.update()






pygame.QUIT() #Encerrar o game