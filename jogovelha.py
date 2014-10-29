#-*-coding:utf-8-*-

tabuleiro =[
    ["","",""],
    ["","",""],
    ["","",""],
]

def desenhaTabuleiro():
    for linha in tabuleiro:
        for valor in linha:
            print(valor + "\t", end="")
        print("\n")


def lerJogada():
    jogadaValida = False
    while not jogadaValida:
        linha = int(input('Digite linha para jogada:'))
        if  linha >= 0 and linha < 3:
            coluna = int(input('Digite coluna para jogada:'))
            if coluna >= 0 and coluna < 3:
                if not tabuleiro[linha][coluna]:
                    jogadaValida = True
                else:
                    print("Jogava não disponível!")
            else:
                print("Coluna Inválida!")
        else:
            print("Linha Inválida!")
    return (linha, coluna)


def verificaVencedor():
#   primeira horizontal
    if  tabuleiro[0][0] == tabuleiro[0][1] and tabuleiro[0][0] == tabuleiro[0][2] and tabuleiro[0][0]:
        return True
#   segunda horizontal
    if  tabuleiro[1][0] == tabuleiro[1][1] and tabuleiro[1][0] == tabuleiro[1][2] and tabuleiro[1][0]:
        return True
#   terceira horizontal
    if  tabuleiro[2][0] == tabuleiro[2][1] and tabuleiro[2][0] == tabuleiro[2][2] and tabuleiro[2][0]:
        return True
#   primeira vertical
    if  tabuleiro[0][0] == tabuleiro[1][0] and tabuleiro[0][0] == tabuleiro[2][0] and tabuleiro[0][0]:
        return True
#   segunda vertical
    if  tabuleiro[0][1] == tabuleiro[1][1] and tabuleiro[0][1] == tabuleiro[2][1] and tabuleiro[0][1]:
        return True
#   terceira vertical
    if  tabuleiro[0][2] == tabuleiro[1][2] and tabuleiro[0][2] == tabuleiro[2][2] and tabuleiro[0][2]:
        return True
#   diagonal principal
    if  tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2] and tabuleiro[0][0]:
        return True
#   diagonal secundaria
    if  tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0] and tabuleiro[0][2]:
        return True
    return False


def main():
    desenhaTabuleiro()
    ganhador = False
    jogada = 1
    while jogada < 10 and not ganhador:
        jogada += 1
        if jogada % 2 == 0:
            jogador = "X"
        else:
            jogador = "O"

        linha, coluna = lerJogada()
        tabuleiro[linha][coluna] = jogador
        ganhador = verificaVencedor()
        desenhaTabuleiro()

    if ganhador:
        print("{0} ganhou!".format(jogador))
    else:
        print("Empate!")

if __name__ == "__main__":
    main()
