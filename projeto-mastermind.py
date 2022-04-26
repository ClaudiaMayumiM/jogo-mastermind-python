def reduz_pinos():
    global chute_usr
    global pino_amr 
    global pino_ver 
    global pino_az 
    global pino_rx 
    global pino_vrml 
    global pino_lar 

    for i in range(len(chute_usr)):
        if chute_usr[i] == 1:
            pino_amr -= 1
        elif chute_usr[i] == 2:
            pino_ver -= 1
        elif chute_usr[i] == 3:
            pino_az -= 1
        elif chute_usr[i] == 4:
            pino_rx -= 1
        elif chute_usr[i] == 5:
            pino_vrml -= 1
        elif chute_usr[i] == 6:
            pino_lar -= 1
    print(f'\nVocê possui:\n{pino_amr} pino(s) amarelo(s)---> 1\n{pino_ver} pino(s) verde(s)---> 2\n{pino_az} pino(s) azuis---> 3\n{pino_rx} pino(s) roxo(s)---> 4\n{pino_vrml} pino(s) vermelho(s)---> 5\n{pino_lar} pino(s) laranja(s)---> 6\n')

def interrompe_pinos():
    global jogo
    global chute_usr
    global pino_amr 
    global pino_ver 
    global pino_az 
    global pino_rx 
    global pino_vrml 
    global pino_lar 
    
    for i in range(len(chute_usr)):
        if pino_amr < 0 and chute_usr[i] == 1:
            print('Você esgotou seus pinos amarelos! É impossível adivinhar a senha!\nO JOGO ACABOU!\n')
            jogo = False
        elif pino_ver < 0 and chute_usr[i] == 2:
            print('Você esgotou seus pinos verdes! É impossível adivinhar a senha!\nO JOGO ACABOU!\n')
            jogo = False
        elif pino_az < 0 and chute_usr[i] == 3:
            print('Você esgotou seus pinos azuis! É impossível adivinhar a senha!\nO JOGO ACABOU!\n')
            jogo = False
        elif pino_rx < 0 and chute_usr[i] == 4:
            print('Você esgotou seus pinos roxos! É impossível adivinhar a senha!\nO JOGO ACABOU!\n')
            jogo = False
        elif pino_vrml < 0 and chute_usr[i] == 5:
            print('Você esgotou seus pinos vermelhos! É impossível adivinhar a senha!\nO JOGO ACABOU!\n')
            jogo = False
        elif pino_lar < 0 and chute_usr[i] == 6:
            print('Você esgotou seus pinos laranjas! É impossível adivinhar a senha!\nO JOGO ACABOU!\n')
            jogo = False

def imprime_instrucao():
    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('Bem vindo ao jogo Mastermind!\n\nO jogo funciona assim:\n\n1 - O computador gera uma senha de quatro cores.\n2 - Existem 6 opções de cores no jogo, e cada uma é representada por um número, sendo:\n1: amarelo, 2: verde, 3: azul, 4: roxo, 5: vermelho, 6: laranja\n3 - Você deve adivinhar a senha gerada pelo computador e terá 3 tentativas para isso!\n')
    print('Além disso, dentro das suas 3 tentativas, você poderá utilizar 3 pinos de cada uma das 6 cores disponíveis!\n')
    print('Você também ganhará dicas a respeito dos chutes realizados:\n\nVocê receberá um pino BRANCO, caso acerte a cor e a posição no seu chute.\n')
    print('Você receberá um pino PRETO, caso acerte a cor, mas não acerte a posição no seu chute.\n\n')
    print('Exemplo de jogo:\n\nsenha a ser adivinhada pelo jogador: 1, 2, 3, 4 ("amarelo, verde, azul, roxo")\n\nchute: 1, 5, 4, 6\n\nO elemento na posição 1 recebe pino BRANCO (acertou a cor e a posição)\nO elemento na posição 3 recebe pino PRETO (acertou a cor mas não acertou a posição)\n\n')
    print('BOA SORTE!\n')
    print('-----------------------------------------------------------------------------------------------------------------------------')


import random

cores = [1, 2, 3, 4, 5, 6]

mapa_cores = {1:'amarelo', 2:'verde', 3:'azul', 4:'roxo', 5:'vermelho', 6:'laranja'}

tentativas = 0 

pino_amr = 3
pino_ver = 3
pino_az = 3
pino_rx = 3
pino_vrml = 3
pino_lar = 3

jogo = True 

senha = random.sample(cores, 4)

imprime_instrucao()

while jogo:
    cor_certa = ''
    chute_cor = ''
    chute_usr = list(map(int, input('Digite uma sequência de quatro cores, dentre as opções: amarelo, verde, azul, roxo, vermelho e laranja.\nUSE = 1: amarelo, 2: verde, 3: azul, 4: roxo, 5: vermelho, 6: laranja\nExemplo: AZUL VERMELHO ROXO LARANJA ---> 3, 5, 4, 6\nSepare o chute apenas por vírgula.\n').strip().split(',')))
    
    if len(chute_usr) != len(senha):
        print('\n***Você deve digitar um palpite de 4 cores!***')
        continue
    elif all(x in cores for x in chute_usr) == False: 
        print('\n***Você deve escolher dentre as opções propostas!***')
        continue
    else:
        tentativas += 1
        reduz_pinos()
        if interrompe_pinos():
            jogo = False
        elif jogo == True:
            print(f'\nPalpite cadastrado! Você está na jogada número: {tentativas}!\nVocê ainda pode realizar {3 - tentativas} jogada(s)!\n')

    print(f'O seu chute foi: {chute_usr}')
    
    if jogo == True:
        if cor_certa != 'BBBB':
            for i in range(4):
                if chute_usr[i] == senha[i]:
                    cor_certa += 'B'
                    print(f'O elemento na posição {i + 1} recebe pino branco!')
                elif chute_usr[i] != senha[i] and chute_usr[i] in senha:
                    chute_cor += 'P'
                    print(f'O elemento na posição {i + 1} recebe pino preto!')
            print(f'Pinos brancos(B) e pretos(P) recebidos: {cor_certa} {chute_cor}\n')

    if cor_certa == 'BBBB':
        if tentativas == 1:
            print('Parabéns, você adivinhou a senha na primeira tentativa!')
        else: 
            print(f'Bom trabalho, você usou {tentativas} jogadas para adivinhar!')
        jogo = False 
    
    if tentativas >= 1 and tentativas < 3 and cor_certa != 'BBBB' and jogo == True:
        print('Próxima jogada!\n')
    elif tentativas > 2 and cor_certa!= 'BBBB':
        print(f'Você não adivinhou a senha! A sequência de cores era: {senha}!')
        jogo = False