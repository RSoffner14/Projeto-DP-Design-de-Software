from random import randint
import copy

m = 0 #
while m < 6:
        m = int(input("Digite um número para o tamanho da sua mesa de jogo.\n"))         

mesa = []

placar_jogo = 0

r = []

for i in range(m):
   r.append(i+1)

u = 0

for f in range(m):
    mesa.append (["+"] * m)
  
mapa_computador = mesa
                 
def mesa_jogo(u, mesa):
    for row in mesa:
        print (" ".join(row), r[u])
        u += 1
print ("\nBem Vindo ao melhor jogo de batalha naval marujo!\n\nNo mapa abaixo existem 6 tipos diferentes de navios.\n\nQuando acertar todos declaro que terá ganho o melhor jogo de batalha naval.\n\nBoa Sorte!\n\nInsira um valor de 1 a", m,"para linhas e colunas e pressione a tecla Enter.\n\nBom jogo marujo!\n")


def position():
    q = randint(0,1) 
    return q
navios=[6,5,4,3,2,1] 

def general_random(mesa):
    b = randint(0, len(mesa) - 1)
    n = randint(0, len(mesa) - 1)
    x=[b,n]
    return x

def put_board(tamanho, mapa_computador):
    p = position()
    x = general_random(mesa)
    mapa_copia = copy.deepcopy(mapa_computador)
       
    try:
        for h in range(tamanho):
            if p == 0:
                while x[0]+tamanho > m:
                    x=general_random(mesa)
                if mapa_copia[x[0]+h][x[1]] == "+":
                    mapa_copia[x[0]+h][x[1]] = tamanho
                else:
                    return put_board(tamanho,mapa_computador)
            else:
                while x[1]+tamanho > m:
                    x=general_random(mesa)
                if mapa_copia[x[0]][x[1]+h] == "+":
                    mapa_copia[x[0]][x[1]+h] = tamanho
                else:
                    return put_board(tamanho,mapa_computador)
        
    except:
        return put_board(tamanho, mapa_computador)  
    return mapa_copia
        

def posicao(navios):
    mapa_computador = []
    for x in range(m):
        mapa_computador.append(["+"]*m)
    for i in navios:
        mapa_computador = put_board(i, mapa_computador)
    
        
    return mapa_computador
        
        
mapa_computador = posicao(navios)
print(mapa_computador)

vez = 1
erradas = m*5

boat_size = {6:6,
             5:5,
             4:4,
             3:3,
             2:2,
             1:1}

pontuacao_barcos = {6:20,
                    5:15,
                    4:10,
                    3:5,
                    2:3,
                    1:1}

while erradas > 0 :
    
    if placar_jogo == 54:
        print ("Todos os navios foram afundados!")        
        print ("\nParabens! Voce ganhou o melhor jogo de batalha naval, Marujo!\n")
            

    print ("\nRodada", vez,"    Placar:",placar_jogo,"\n")
    mesa_jogo(u, mesa)
            
      
    chute_coluna = int(input("Coluna:\n")) - 1
    while chute_coluna < 0 or chute_coluna > m-1:
        print ("\nFora da mesa de jogo! Tente com numeros menores\n")    
        chute_coluna = int(input("Coluna:\n")) - 1
        
    chute_linha = int(input("\nLinha:\n")) -1
    while chute_linha < 0 or chute_linha > m-1:
        print ("\nFora da mesa de jogo! Tente com numeros menores\n")
        chute_linha = int(input("\nLinha:\n")) -1
        
   
    print ("Rodada",vez, "    Placar:",placar_jogo)

                    
    if(mesa[chute_linha][chute_coluna] == "X" or mesa[chute_linha][chute_coluna] == "o"):
            print ("\nJá tentou nesse ponto marujo! Tente novamente")
            
    else:    
        if mapa_computador[chute_linha][chute_coluna] == "+":
            print ("\nERROOUUUU, água!")
            mesa[chute_linha][chute_coluna] = "o"
            erradas -= 1
    
        elif mapa_computador[chute_linha][chute_coluna] != "+":
            print ("\nAcertou o ponto do meu navio, marujo!")
            barco = mapa_computador[chute_linha][chute_coluna]
            boat_size[barco] -= 1
            
            if boat_size[barco]==0:
                print ("\nAfundou meu navio marujo, parabenss!")
                placar_jogo += pontuacao_barcos[barco]
            mesa[chute_linha][chute_coluna] = "X"
    
print ("Fim de jogo!") 