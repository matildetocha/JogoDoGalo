# Matilde Tocha 99108

def eh_posicao_marcada(pm):
    """ Pretende descobrir se o argumento inserido e ou nao uma posicao marcada.

    :param pm: Um int, posicao marcada. (-1 ou 1).
    :return: Um bool, veracidade do argumento.
    """
    if type(pm) != int or pm != 1 and pm != -1:
        return False
    return True


def eh_tabuleiro(tab):
    """ Pretende descobrir se o argumento inserido e ou nao um tabuleiro.

    :param tab: Um tuple constituido por 3 tuples, tabuleiro.
    :return: Um bool, veracidade do argumento.
    """
    if not isinstance(tab, tuple) or len(tab) != 3:
        return False
    for i in tab:
        if not isinstance(i, tuple) or len(i) != 3:
            return False
        for e in i:
            if type(e) != int or not eh_posicao_marcada(e) and e != 0:
                return False
    return True


def eh_posicao(p):
    """ Pretende descobrir se o argumento inserido e ou nao uma posicao de um tabuleiro.

    :param p: Um int, posicao de um tabuleiro (1 a 9).
    :return: Um bool, veracidade do argumento.
    """
    if type(p) != int:
        return False
    elif not 1 <= p <= 9:  # posicoes de 1 a 9
        return False
    return True


def obter_coluna(tab, c):
    """ Recebe um tabuleiro e o valor de uma coluna devolve um vetor com os valores da coluna pretendida do tabuleiro.

    :param tab: Um tuple, tabuleiro.
    :param c: Um int, valor da coluna do tabuleiro (1 a 3).
    :return: Um tuple, coluna do tabuleiro.
    """
    if not eh_tabuleiro(tab) or type(c) != int or not 1 <= c <= 3:
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    coluna = ()
    for i in range(len(tab)):
        e = c - 1                   # retira o elemento correspondente a coluna inserida de cada linha do tab
        coluna += (tab[i][e], )
    return coluna


def obter_linha(tab, li):
    """ Recebe um tabuleiro e o valor de uma linha e devolve um vetor com os valores da linha pretendida do tabuleiro.

    :param tab: Um tuple, tabuleiro.
    :param li: Um int, valor da linha do tabuleiro. (1 a 3).
    :return: Um tuple, linha do tabuleiro.
    """
    if not eh_tabuleiro(tab) or type(li) != int or not 1 <= li <= 3:
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    for i in range(len(tab)):
        i = li - 1                # linhas = 3 tuplos de tab
        return tab[i]


def obter_diagonal(tab, d):
    """ Recebe um tabuleiro e o valor de uma diagonal e devolve um vetor com os valores da diagonal
    pretendida do tabuleiro.

    :param tab: Um tuple, tabuleiro.
    :param d: Um int, valor da diagonal do tabuleiro. 1 para a diagonal
              descendente da esquerda para a direita e 2 para a diagonal
              ascendente da esquerda para a direita.
    :return: Um tuple, diagonal do tabuleiro.
    """
    if not eh_tabuleiro(tab) or type(d) != int or not 1 <= d <= 2:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    res = ()
    e = - 1
    for i in range(len(tab)):
        if d == 1:
            e += 1                   # retira os elementos da diagonal 1
            res += (tab[i][e], )
        elif d == 2:
            tab = tab[::-1]          # inverte a ordem de tab
            e += 1                   # retira os elementos da diagonal 2
            res += (tab[i][e], )
    return res


def tabuleiro_posicoes(tab):
    """ Recebe um tabuleiro e devolve um tuplo com as posicoes de um tabuleiro, cujos index vao de 0 a 8,
    de modo a obter as posicoes de cada posicao marcada.

    :param tab: Um tuple, tabuleiro.
    :return: Um tuple, tabuleiro com index de posicoes.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_posicoes: o argumento e invalido')
    tab_p = ()
    for i in tab:
        for e in i:
            tab_p += (e, )
    return tab_p


def tabuleiro_str(tab):
    """ Recebe um tabuleiro e devolve a representacao externa do tabuleiro.

    :param tab: Um tuple, tabuleiro.
    :return: Uma str, tabuleiro convertido para a representacao externa.
    """
    def posicao_str(p):
        """ Funcao auxiliar, converte as posicoes marcadas ou livres na sua representacao externa.

        :param p: Um int, posicao marcada ou livre do tabuleiro.
        :return: Uma str, posicao convertida para a representacao externa.
        """
        if not eh_posicao_marcada(p) and p != 0:
            raise ValueError('posicao_str: o argumento e invalido')
        elif p == 1:
            return 'X'
        elif p == - 1:
            return 'O'
        elif p == 0:
            return ' '
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    tab_rep = ''
    for i in tab:
        for e in i:
            tab_rep += posicao_str(e)
            # converte os valores das posicoes do tabuleiro e guarda-os numa string
    return ' ' + tab_rep[0] + ' | ' + tab_rep[1] + ' | ' + tab_rep[2] + ' \n-----------\n ' + tab_rep[3] + ' | ' +\
           tab_rep[4] + ' | ' + tab_rep[5] + ' \n-----------\n ' + tab_rep[6] + ' | ' + tab_rep[7] + ' | ' +\
           tab_rep[8] + ' '


def converte_posicao(tab, p):
    """ Recebe um tabuleiro e uma posicao do tabuleiro e converte o valor da posicao de um tabuleiro numa
    posicao marcada de -1 a 1

    :param tab: Um tuple, tabuleiro.
    :param p: Um int, posicao do tabuleiro.
    :return: Um int, posicao marcada do tabuleiro.
    """
    if not eh_tabuleiro(tab) or not eh_posicao(p):
        raise ValueError('converte_posicao: algum dos argumentos e invalido')
    p_linha = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3}
    # dicionario de linhas para cada posicao 1 a 9
    p_coluna = {1: 1, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 2, 9: 3}
    # dicionario de colunas para cada posicao 1 a 9
    return obter_linha(tab, p_linha[p])[p_coluna[p] - 1]


def eh_posicao_livre(tab, p):
    """ Recebe um tabuleiro e uma posicao do tabuleiro e pretende descobrir se a posicao inserida corresponde ou nao a
    uma posicao livre do tabuleiro. Livre se a posicao for igual a 0.

    :param tab: Um tuple, tabuleiro.
    :param p: Um int, posicao do tabuleiro.
    :return: Um bool, veracidade do argumento.
    """
    if not eh_tabuleiro(tab) or not eh_posicao(p):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    if converte_posicao(tab, p) == 1 or converte_posicao(tab, p) == - 1:
        return False
    return True


def obter_posicoes_livres(tab):
    """ Recebe um tabuleiro e devolve um vetor ordenado com todas a posicoes livres do tabuleiro.

    :param tab: Um tuple, tabuleiro.
    :return: Um tuple, posicoes livres do tabuleiro.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    posicoes_livres = ()
    for p in range(len(tabuleiro_posicoes(tab))):    # 0 <= p <= 8
        if eh_posicao_livre(tab, p + 1):
            posicoes_livres += (p + 1, )
    return posicoes_livres


def jogador_ganhador(tab):
    """ Recebe um tabuleiro e devolve um valor inteiro a indicar o jogador que ganhou a partida,
    sendo o valor igual a 1 se ganhou o jogador que joga com 'X', -1 se ganhou o jogador que joga com 'O',
    ou 0 se nenhum jogador ganhou.

    :param tab: Um tuple, tabuleiro.
    :return: Um int, jogador ganhador da partida.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')
    for n in range(1, 4):
        linha = obter_linha(tab, n)
        coluna = obter_coluna(tab, n)
        if linha[0] == linha[1] == linha[2]:
            return linha[0]
        elif coluna[0] == coluna[1] == coluna[2]:
            return coluna[0]
    for d in range(1, 3):
        diagonal = obter_diagonal(tab, d)
        if diagonal[0] == diagonal[1] == diagonal[2]:
            return diagonal[0]
    return 0


def marcar_posicao(tab, pm, pl):
    """ Recebe um tabuleiro, jogador e posicao do tabuleiro e devolve um tabuleiro modificado com a nova
    marca do jogador numa posicao, ou seja, apos a jogada do mesmo.

    :param tab: Um tuple, tabuleiro.
    :param pm: Um int, identificacao do jogador. 1 para o jogador 'X' e -1 para o jogador 'O'.
    :param pl: Um int, posicao livre do tabuleiro.
    :return: Um tuple, tabuleiro modificado.
    """
    if not eh_tabuleiro(tab) or not eh_posicao_marcada(pm) or not eh_posicao(pl) or not eh_posicao_livre(tab, pl):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    new_tab = ()
    for i in range(len(tabuleiro_posicoes(tab))):    # 0 <= i <= 8
        if i == pl - 1:
            new_tab += (pm, )
        else:
            new_tab += (tabuleiro_posicoes(tab)[i], )
    return (new_tab[0:3], ) + (new_tab[3:6], ) + (new_tab[6:9], )


def escolher_posicao_manual(tab):
    """ Realiza a leitura de uma posicao introduzida manualmente por um jogador e devolve essa posicao escolhida.

    :param tab: Um tuple, tabuleiro.
    :return: Um int, posicao escolhida manualmente pelo jogador.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_manual: o argumento e invalido')
    p = int(input('Turno do jogador. Escolha uma posicao livre: '))
    if not eh_posicao(p) or not eh_posicao_livre(tab, p):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    return p


def vitoria(tab, pm):
    """ Recebe um tabuleiro e um jogador. Criterio de estrategia: se o jogador tiver duas das suas pecas em linha
    e uma posicao livre, entao devolve essa posicao livre (ganhando o jogo).

    :param tab: Um tuple, tabuleiro.
    :param pm: Um int, identificacao do jogador. 1 para o jogador 'X' e -1 para o jogador 'O'.
    :return: Uma lst, posicoes livres que devem ser marcadas pelo jogador.
    """
    if not eh_tabuleiro(tab) or not eh_posicao_marcada(pm):
        raise ValueError('vitoria: algum dos argumentos e invalido')
    pos = []    # possibilidades de vitoria
    for i in range(1, 4):
        linha = obter_linha(tab, i)
        coluna = obter_coluna(tab, i)
        # testar linhas
        if linha[0] == linha[1] == pm and eh_posicao_livre(tab, i * 3):
            pos += [i * 3]
        elif linha[0] == linha[2] == pm and eh_posicao_livre(tab, i * 3 - 1):
            pos += [i * 3 - 1]
        elif linha[1] == linha[2] == pm and eh_posicao_livre(tab, i * 3 - 2):
            pos += [i * 3 - 2]
        # testar colunas
        elif coluna[0] == coluna[1] == pm and eh_posicao_livre(tab, i + 6):
            pos += [6 + i]
        elif coluna[0] == coluna[2] == pm and eh_posicao_livre(tab, i + 3):
            pos += [3 + i]
        elif coluna[1] == coluna[2] == pm and eh_posicao_livre(tab, i):
            pos += [i]
    for i in range(1, 3):
        diagonal = obter_diagonal(tab, i)
        # testar diagonais
        if diagonal[0] == diagonal[1] == pm and eh_posicao_livre(tab, 10 // i - i):
            pos += [10 // i - i]
        elif diagonal[0] == diagonal[2] == pm and eh_posicao_livre(tab, 5):
            pos += [5]
        elif diagonal[1] == diagonal[2] == pm and eh_posicao_livre(tab, i ** 3 - (i - 1)):
            pos += [i ** 3 - (i - 1)]
    return sorted(pos)


def bloqueio(tab, pm):
    """ Recebe um tabuleiro e um jogador. Criterio de estrategia: se o adversario tiver duas das suas pecas
    em linha e uma posicao livre, entao devolve essa posicao livre (bloqueando a vitoria do adversario).

    :param tab: Um tuple, tabuleiro.
    :param pm: Um int, identificacao do jogador. 1 para o jogador 'X' e -1 para o jogador 'O'.
    :return: Uma lst, posicoes livres que devem ser marcadas pelo jogador.
    """
    if not eh_tabuleiro(tab) or not eh_posicao_marcada(pm):
        raise ValueError('bloqueio: algum dos argumentos e invalido')
    if pm == 1:
        return vitoria(tab, -1)
    elif pm == -1:
        return vitoria(tab, 1)


def bifurcacao(tab, pm):
    """ Recebe um tabuleiro e um jogador. Criterio de estrategia: se o jogador tiver duas linhas/ colunas/ diagonais
    que se intersetam, onde cada uma contem uma das suas pecas e a posicao de intersecao estiver livre, entao devolve
    essa posicao livre (criando 2 formas de ganhar).

    :param tab: Um tuple, tabuleiro.
    :param pm: Um int, identificacao do jogador. 1 para o jogador 'X' e -1 para o jogador 'O'.
    :return: Uma lst, posicoes livres que devem ser marcadas pelo jogador.
    """
    if not eh_tabuleiro(tab) or not eh_posicao_marcada(pm):
        raise ValueError('bifurcacao: algum dos argumentos e invalido')
    pos = []    # lista de possibilidades de bifurcacao
    # testar linhas com colunas
    for i in range(1, 4):
        if pm in obter_linha(tab, 1) and pm in obter_coluna(tab, i) and eh_posicao_livre(tab, i):
            # se a jogador tiver uma pm na linha 1 e numa coluna, a intersecao e uma bifurcacao
            if -pm in obter_linha(tab, 1) or -pm in obter_coluna(tab, i):
                # so pode ser bifurcacao se o adversario nao tiver uma pm nessa linha ou coluna
                pos += []
            else:
                pos += [i]
    for i in range(1, 4):
        if pm in obter_linha(tab, 2) and pm in obter_coluna(tab, i) and eh_posicao_livre(tab, i + 3):
            # se a jogador tiver uma pm na linha 2 e numa coluna, a intersecao e uma bifurcacao
            if -pm in obter_linha(tab, 2) or -pm in obter_coluna(tab, i):
                # so pode ser bifurcacao se o adversario nao tiver uma pm nessa linha ou coluna
                pos += []
            else:
                pos += [i + 3]
    for i in range(1, 4):
        if pm in obter_linha(tab, 3) and pm in obter_coluna(tab, i) and eh_posicao_livre(tab, i + 6):
            # se a jogador tiver uma pm na linha 3 e numa coluna, a intersecao e uma bifurcacao
            if -pm in obter_linha(tab, 3) or -pm in obter_coluna(tab, i):
                # so pode ser bifurcacao se o adversario nao tiver uma pm nessa linha ou coluna
                pos += []
            else:
                pos += [i + 6]
    # testar diagonais com linhas e colunas
    for i in range(1, 4):
        if (pm in obter_diagonal(tab, 1) and pm in obter_linha(tab, i)) \
                or (pm in obter_diagonal(tab, 1) and pm in obter_coluna(tab, i)):
            # se a jogador tiver uma pm na diagonal 1 e numa linha / coluna, a intersecao e uma bifurcacao
            if eh_posicao_livre(tab, -3 + 4 * i):
                if (-pm in obter_diagonal(tab, 1) or -pm in obter_linha(tab, i)) and \
                        (-pm in obter_diagonal(tab, 1) or -pm in obter_coluna(tab, i)):
                    # so pode ser bifurcacao se o adversario nao tiver uma pm nessa diagonal ou linha/ coluna
                    pos += []
                else:
                    pos += [-3 + 4 * i]
    for i in range(1, 4):
        if pm in obter_diagonal(tab, 2) and pm in obter_linha(tab, i) and eh_posicao_livre(tab, 1 + 2 * i):
            # se a jogador tiver uma pm na diagonal 2 e numa linha, a intersecao e uma bifurcacao
            if -pm in obter_diagonal(tab, 2) or -pm in obter_linha(tab, i):
                # so pode ser bifurcacao se o adversario nao tiver uma pm nessa diagonal ou linha
                pos += []
            else:
                pos += [1 + 2 * i]
    for i in range(1, 4):
        if pm in obter_diagonal(tab, 2) and pm in obter_coluna(tab, i) and eh_posicao_livre(tab, -2 * i + 9):
            # se a jogador tiver uma pm na diagonal 2 e numa coluna, a intersecao e uma bifurcacao
            if -pm in obter_diagonal(tab, 2) or -pm in obter_coluna(tab, i):
                # so pode ser bifurcacao se o adversario nao tiver uma pm nessa diagonal ou coluna
                pos += []
            else:
                pos += [-2 * i + 9]
    return sorted(pos)


def bloqueio_bifurcacao(tab, pm):
    """ Recebe um tabuleiro e um jogador. Criterio de estrategia: se o adversario tiver apenas uma bifurcacao,
    entao devolve essa posicao livre de intersecao (de modo a bloquear a jogada do adversario). Senao devolve
    uma posicao livre que faca um dois em linha.

    :param tab: Um tuple, tabuleiro.
    :param pm: Um int, identificacao do jogador. 1 para o jogador 'X' e -1 para o jogador 'O'.
    :return: Um int, posicao livre que deve ser marcada pelo jogador OU
            Uma lst, posicoes livres que devem ser marcadas pelo jogador.
    """
    def canto_contrario(tab, pm):
        """ Funcao auxiliar, uma lista com todos os cantos contrarios livres.
        (canto contrario = simetria de reflexao das linhas/ colunas)

        :param tab: Um tuple, tabuleiro.
        :param pm: Um int, identificacao do jogador. 1 para o jogador 'X' e -1 para o jogador 'O'.
        :return: Uma lst, cantos contrarios livres.
        """
        tab_p = tabuleiro_posicoes(tab)
        pos = []  # possibilidades de cantos contrarios livres
        if tab_p[0] == pm or tab[8] == pm and eh_posicao_livre(tab, 3):
            pos += [3]
        elif tab_p[2] == pm or tab[6] == pm and eh_posicao_livre(tab, 1):
            pos += [1]
        elif tab_p[0] == pm or tab[8] == pm and eh_posicao_livre(tab, 8):
            pos += [8]
        elif tab_p[2] == pm or tab[6] == pm and eh_posicao_livre(tab, 9):
            pos += [9]
        return sorted(pos)
    if not eh_tabuleiro(tab) or not eh_posicao_marcada(pm):
        raise ValueError('bloqueio_bifurcacao: algum dos argumentos e invalido')
    if pm == 1:
        if len(bifurcacao(tab, -1)) > 1:    # advesario tem mais de que 1 bifurcacao possivel
            if converte_posicao(tab, 5) == 1:
                return lateral_vazio(tab)
            elif converte_posicao(tab, 5) == -1:
                return canto_contrario(tab, pm)
        else:
            return bifurcacao(tab, -1)
    elif pm == -1:
        if len(bifurcacao(tab, 1)) > 1:     # advesario tem mais de que 1 bifurcacao possivel
            if converte_posicao(tab, 5) == -1:
                return lateral_vazio(tab)
            elif converte_posicao(tab, 5) == 1:
                return canto_contrario(tab, pm)
        else:
            return bifurcacao(tab, 1)


def centro(tab):
    """ Recebe um tabuleiro. Criterio de estrategia: se a posicao central estiver livre,
    entao devolve essa posicao livre.

    :param tab: Um tuple, tabuleiro
    :return: Um int, posicao livre que deve ser marcada pelo jogador.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('centro: o argumento e invalido')
    elif eh_posicao_livre(tab, 5):
        return 5


def canto_oposto(tab, pm):
    """ Recebe um tabuleiro e um jogador. Criterio de estrategia: se o adversario estiver num canto e o
    canto diagonalmente oposto for uma posicao livre, entao devolve essa posicao livre.

    :param tab: Um tuple, tabuleiro.
    :param pm: Um int, identificacao do jogador. 1 para o jogador 'X' e -1 para o jogador 'O'.
    :return: Um int, posicao livre que deve ser marcada pelo jogador.
    """
    if not eh_tabuleiro(tab) or not eh_posicao_marcada(pm):
        raise ValueError('canto_oposto: algum dos argumentos e invalido')
    tab_p = tabuleiro_posicoes(tab)
    if tab_p[0] != pm and eh_posicao_marcada(tab_p[0]) and eh_posicao_livre(tab, 9):
        return 9
    elif tab_p[2] != pm and eh_posicao_marcada(tab_p[2]) and eh_posicao_livre(tab, 7):
        return 7
    elif tab_p[6] != pm and eh_posicao_marcada(tab_p[6]) and eh_posicao_livre(tab, 3):
        return 3
    elif tab_p[8] != pm and eh_posicao_marcada(tab_p[8]) and eh_posicao_livre(tab, 1):
        return 1


def canto_vazio(tab):
    """ Recebe um tabuleiro. Criterio da estrategia: se um canto for uma posicao livre,
    entao devolve essa posicao livre.

    :param tab: Um tuple, tabuleiro.
    :return: Um int, posicao livre que deve ser marcada pelo jogador.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('canto_vazio: o argumento e invalido')
    cantos = (1, 3, 7, 9)
    for e in cantos:
        if eh_posicao_livre(tab, e) is True:
            return e


def lateral_vazio(tab):
    """ Recebe um tabuleiro. Criterio da estrategia: se uma posicao lateral for livre,
    entao devolve essa posicao livre.

    :param tab: Um tuple, tabuleiro.
    :return: Um int, posicao livre que deve ser marcada pelo jogador.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('lateral_vazio: o argumento e invalido')
    laterais = (2, 4, 6, 8)
    for e in laterais:
        if eh_posicao_livre(tab, e) is True:
            return e


def eh_estrategias(estr):
    """ Pretende descobrir se o argumento inserido e ou nao uma estrategia de jogo.

    :param estr: Uma str, estrategia de jogo.
    :return: Um bool, veracidade do argumento.
    """
    if not isinstance(estr, str) or estr != 'basico' and estr != 'normal' and estr != 'perfeito':
        return False
    return True


def escolher_posicao_auto(tab, pm, estr):
    """ Recebe um tabuleiro, um jogador, e uma estrategia e escolhe uma posicao automaticamente,
    de acordo com os parametros inseridos.

    :param tab: Um tuple, tabuleiro.
    :param pm: Um int, posicao marcada.
    :param estr: Uma str, estrategia de jogo.
    :return: Um int, posicao escolhida automaticamente.
    """
    if not eh_tabuleiro(tab) or not eh_posicao_marcada(pm) or not eh_estrategias(estr):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    elif estr == 'basico':
        return centro(tab) or canto_vazio(tab) or lateral_vazio(tab)   # ordem das estrategias 'basico'
    elif estr == 'normal':
        if len(vitoria(tab, pm)) >= 1:          # ordem das estrategias 'normal'
            return vitoria(tab, pm)[0]
        elif len(bloqueio(tab, pm)) >= 1:
            return bloqueio(tab, pm)[0]
        else:
            return centro(tab) or canto_oposto(tab, pm) or canto_vazio(tab) or lateral_vazio(tab)
    elif estr == 'perfeito':
        if len(vitoria(tab, pm)) >= 1:         # ordem das estrategias 'perfeito'
            return vitoria(tab, pm)[0]
        elif len(bloqueio(tab, pm)) >= 1:
            return bloqueio(tab, pm)[0]
        elif len(bifurcacao(tab, pm)) >= 1:
            return bifurcacao(tab, pm)[0]
        elif bloqueio_bifurcacao(tab, pm) or len(bloqueio_bifurcacao(tab, pm)) >= 1:
            return bloqueio_bifurcacao(tab, pm) or bloqueio_bifurcacao(tab, pm)[0]
        else:
            return centro(tab) or canto_oposto(tab, pm) or canto_vazio(tab) or lateral_vazio(tab)


def jogo_do_galo(player, estr):
    """ Funcao principal do jogo, permite jogar um jogo completo de Jogo do Galo
    de um jogador contra o computador.

    :param player: Uma str, identificacao do jogador.
    :param estr: Uma str, estrategia de jogo.
    :return: Uma str, jogo completo
    """
    def player_pm(player):
        """ Funcao auxiliar, converte a identificacao do jogador (str) em posicoes marcadas (int).

        :param player: Uma str, identificacao do jogador
        :return: Um int, posicao marcada.
        """
        if player == 'X':
            return 1
        elif player == 'O':
            return -1
    if not isinstance(player, str) or player != 'X' and player != 'O' or not eh_estrategias(estr):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    print('Bem-vindo ao JOGO DO GALO.' + '\n' + 'O jogador joga com \'' + player + '\'.')
    t = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    while len(obter_posicoes_livres(t)) > 0:
        if player == 'X':
            pc = 'O'                # se o jogador for o 'X', entao o pc joga com 'O'
            p = escolher_posicao_manual(t)
            print(tabuleiro_str(marcar_posicao(t, player_pm(player), p)))    # apos o jogador escolher a posicao de
            t = marcar_posicao(t, player_pm(player), p)               # jogada o tabuleiro e modificado e representado
            if jogador_ganhador(t) == player_pm(player):
                return player    # se o jogador ganhar o jogo acaba
            elif len(obter_posicoes_livres(t)) == 0:
                return 'EMPATE'    # se ja nao houver mais posicoes livres o jogo acaba
            p = escolher_posicao_auto(t, player_pm(pc), estr)
            print('Turno do computador' + ' ' + '(' + estr + '):' + '\n' +    # apos o pc escolher uma posicao
                  tabuleiro_str(marcar_posicao(t, player_pm(pc), p)))        # de jogada (auto) o tabuleiro e
            t = marcar_posicao(t, player_pm(pc), p)                         # modificado e representado
            if jogador_ganhador(t) == player_pm(pc):
                return pc      # se o pc ganhar o jogo acaba
        else:
            pc = 'X'               # se o jogador for o 'X', entao o pc joga com 'O'
            p = escolher_posicao_auto(t, player_pm(pc), estr)
            print('Turno do computador' + ' ' + '(' + estr + '):' + '\n' +       # apos o pc escolher uma posicao
                  tabuleiro_str(marcar_posicao(t, player_pm(pc), p)))           # de jogada (auto) o tabuleiro e
            t = marcar_posicao(t, player_pm(pc), p)                            # modificado e representado
            if jogador_ganhador(t) == player_pm(pc):
                return pc       # se o pc ganhar o jogo acaba
            elif len(obter_posicoes_livres(t)) == 0:
                return 'EMPATE'    # se ja nao houver mais posicoes livres o jogo acaba
            p = escolher_posicao_manual(t)                                    # apos o jogador escolher a posicao de
            print(tabuleiro_str(marcar_posicao(t, player_pm(player), p)))     # jogada o tabuleiro e modificado e
            t = marcar_posicao(t, player_pm(player), p)                       # representado
            if jogador_ganhador(t) == player_pm(player):
                return player     # se o jogador ganhar o jogo acaba
    return 'EMPATE'     # se ja nao houver mais posicoes livres o jogo acaba
