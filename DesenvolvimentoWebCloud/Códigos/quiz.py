def quiz_simples():
    categorias = {
        'Historia': [
            {'pergunta': 'Quem foi o primeiro presidente do Brasil?', 'resposta': 'Deodoro da Fonseca'},
            {'pergunta': 'Em que ano ocorreu a Independência do Brasil?', 'resposta': '1822'},
        ],
        'Matematica': [
            {'pergunta': 'Quanto é 2 + 2?', 'resposta': '4'},
            {'pergunta': 'Qual é a raiz quadrada de 25?', 'resposta': '5'},
        ],
        'Ciencia': [
            {'pergunta': 'Qual é o símbolo químico do hidrogênio?', 'resposta': 'H'},
            {'pergunta': 'Quem propôs a teoria da relatividade?', 'resposta': 'Albert Einstein'},
        ]
    }

    acertos = 0
    quiz = True

    while quiz:
        try:
            for categoria, perguntas in categorias.items():
                print(f'Categoria: {categoria}')

                for pergunta_atual in perguntas:
                    print(pergunta_atual['pergunta'])
                    resposta_usuario = input('Sua resposta: ')

                    if resposta_usuario.lower() == pergunta_atual['resposta'].lower():
                        print('Resposta correta! Parabéns!')
                        acertos += 1
                    else:
                        print(f'Resposta incorreta. A resposta correta era: {pergunta_atual["resposta"]}')
            if acertos > 4:
                print("parabens você passou!!")
                break
            else:
                print("\nVocê não atingiu os pontos necessários para passar. Tente novamente.\n")
        except KeyboardInterrupt:
            while True:
                print("Quer mesmo sair do jogo? S/N")
                sair = input().lower()
                if sair == "s":
                    quiz = False
                    break
                elif sair == "n":
                    print("Voltando para o quiz ...")
                    break
                else:
                    print("opção invalida. escolha s ou n")

quiz_simples()