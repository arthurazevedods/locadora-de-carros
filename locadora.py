import os

# Lista de jogos disponíveis para alugar
jogos = [
        ("The Legend of Zelda: Breath of the Wild", 25), 
        ("The Witcher 3: Wild Hunt", 20), 
        ("God of War", 30),
        ("Red Dead Redemption 2", 35), 
        ("Horizon Zero Dawn", 20), 
        ("Final Fantasy VII Remake", 25), 
        ("Spider-Man: Miles Morales", 30), 
        ("Resident Evil Village", 28)
        ]

alugados = []

def mostrar_lista_de_jogos(lista_de_jogos):
    for i, jogo in enumerate(lista_de_jogos):
        print("[{}] {} - R$ {} /dia.".format(i, jogo[0], jogo[1]))

while True:
    print('\n\n')
    print("=========")
    print("Bem-vindo à locadora de jogos!")
    print("=========")
    print("O que deseja fazer?")
    print("0 - Mostrar catálogo | 1 - Alugar um jogo | 2 - Devolver um jogo")
    op = int(input())

    print('\n\n')
    if op == 0:
        mostrar_lista_de_jogos(jogos)

    elif op == 1:
        mostrar_lista_de_jogos(jogos)
        print("==========")
        print("Escolha o código do jogo:")
        cod_jogo = int(input())
        print("Por quantos dias você deseja alugar este jogo?")
        dias = int(input())
        print('\n\n')

        print("Você escolheu {} por {} dias.".format(jogos[cod_jogo][0], dias))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * jogos[cod_jogo][1]))

        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print("Parabéns, você alugou o jogo {} por {} dias.".format(jogos[cod_jogo][0], dias))
            alugados.append(jogos.pop(cod_jogo)) # Remove da lista de jogos e coloca em alugados

    elif op == 2:
        if len(alugados) == 0:
            print("Não há jogos para devolver.")
        else:
            print("Segue a lista de jogos alugados. Qual você deseja devolver?")
            mostrar_lista_de_jogos(alugados)
            print("")
            print("Escolha o código do jogo que deseja devolver:")
            cod = int(input())
            print("Obrigado por devolver o jogo {}".format(alugados[cod][0]))
            jogos.append(alugados.pop(cod)) # Remove da lista de alugados e devolve para a lista de jogos disponíveis
    
    print("")
    print("===========")
    print("0 para CONTINUAR | 1 para SAIR")
    if float(input()) == 1:
        break
