'''
Projeto 1 de Fundamentos de Programação
ist1109947 Shimeizi Jin 
'''

'''
2.1.1. eh_territorio: universal → booleano
eh_territorio(arg) recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde 
a um território e False caso contrário.
'''

def eh_territorio(arg):
    # Verifique se arg é um tuplo
    if not isinstance(arg, tuple):
        return False
    # o arg tem de ter pelo menos um caminho vertical e um caminho horizontal
    # o arg não pode ser vazio
    if arg == ():
        return False
    else:
        for vertical in arg:
            if not isinstance(vertical, tuple): # Verifique se o que está dentro dos tuplos é um tuplo
                return False
    
    Nv = len(arg) # Número de caminhos verticais 
    Nh = len(arg[0]) # Número de caminhos horizontais
    # O número de caminhos verticais está entre 1 e 26 (A até Z)
    # O número de caminhos horizontais está entre 1 e 99 
    
    if not (0 < Nv <= 26 and 0 <= Nh <= 99): 
        return False
    
    for i in range(Nv):
        if len(arg[0]) != len(arg[i]): # Verifique se as linhas têm o mesmo número de colunas
            return False
    
    for vertical in arg:
        for horizontal in vertical:
            # Verifique se os elementos internos são inteiros e elementos só pode ser 0 ou 1
            if not (isinstance(horizontal, int) and horizontal in (0, 1)): 
                return False
    else:
        return True
    

'''
2.1.2. obtem_ultima_intersecao: territorio → intersecao
obtem_ultima_intersecao(t) recebe um território e devolve a interseção do extremo superior direito 
do território
'''

def obtem_ultima_intersecao(t):
    
    Nv = len(t) # Número de caminhos verticais 
    Nh = len(t[0]) # Número de caminhos horizontais

    # Obtem última interseção
    letra = chr(Nv - 1 + ord('A')) # Converter número em letra
    numero = Nh 
    return letra, numero


'''
2.1.3. eh_intersecao: universal → booleano 
eh_intersecao(arg) recebe um argumento de qualquer tipo e devolve True
se o seu argumento corresponde a uma interseção e False caso contrário
'''

def eh_intersecao(arg):

    #Verifique se arg é um tuplo
    if not isinstance(arg, tuple):
        return False
    
    # Verifique se o arg tem dois elementos (letra, numero)
    if len(arg) != 2:
        return False
    
    # Verifique se o primeiro elemento é uma letra e o segundo elemento é um número
    if not (isinstance(arg[0], str) and isinstance(arg[1], int)) or len(arg[0]) != 1:
        return False
    
    # Verifique se o caminho vertical é identificado por letras maiusculas de A até Z
    # Verifique se o caminho horizontal é identificado por número inteiro de 1 até 99
    if not ('A' <= arg[0] <= 'Z' and 1 <= arg[1] <= 99):
        return False
    
    else:
        return True


'''
2.1.4. eh_intersecao_valida: territorio × intersecao → booleano
eh_intersecao valida(t, i) recebe um território e uma interseção, e devolve True se a interseção
corresponde a uma interseçãao do território, e False caso contrário
'''

def eh_intersecao_valida(t, i):
    # Verifique se i é uma interseção
    if not eh_intersecao(i):
        return False

    coluna = ord(i[0]) - 65 # Converter a letra em número(índice)
    linha = i[1] 

    # Verifique a interseção é válido para território t
    if not (0 <= coluna < len(t) and 1 <= linha <= len(t[0])):
        return False
    else:
        return True

 
'''
2.1.5. eh_intersecao_livre: territorio × intersecao → booleano
eh_intersecao livre(t, i) recebe um território e uma interseção do territºorio, e devolve True se a interseção
corresponde a uma interseção livre (não ocupada por montanhas) dentro do território e False caso contrário.
'''

def eh_intersecao_livre(t, i):

    coluna = ord(i[0]) - 65 # Converter a letra em número(índice)
    linha = i[1] - 1 # Índice começa do 0

    # Verifique se o caminho vertical e o caminho horizontal é válido para território t
    if len(t) <= coluna or len(t[0]) <= linha:
        return False

    # Verifique se a interseção corresponde a uma interseção livre
    if t[coluna][linha] == 1: # Se 1 então a interseção é ocupada
        return False
    else:
        return True


'''
2.1.6. obtem_intersecoes_adjacentes: territorio × intersecao → tuplo
obtem_intersecoes_adjacentes(t, i) recebe um território e uma interseção do território, e devolve o 
tuplo formadopelas interseções válidas adjacentes da interseção em ordem de leitura de um território.
'''

def obtem_intersecoes_adjacentes(t, i):

    adjacentes = [] # Uma lista vaazia para receber interseções adjacentes
    letra, numero = i # Interseção i(letra, número)
    horizontal = ord(letra) - ord('A') # converter letra em número
    vertical = numero 

    # Verifique interseção acima (se v > 0)
    if 1 < vertical <= len(t[0]): # Permite não objeter interseções que estão fora do limite do território
        adjacentes.append((letra, numero - 1)) # Se interseção adjacente existe adiciona na lista

    # Verifique interseção à esquerda (se h > 0)
    if 0 < horizontal <= len(t) - 1:
        adjacentes.append((chr(ord(letra) - 1), numero))

    # Verifique interseção à direita (se h < Nh - 1)
    if 0 <= horizontal < len(t) - 1:
        adjacentes.append((chr(ord(letra) + 1), numero))
    
    # Verifique interseção abaixo (se v < Nv - 1)
    if 0 <= vertical < len(t[0]):
        adjacentes.append((letra, numero + 1))
    return tuple(adjacentes) # Obtem interseções adjacentes


'''
2.1.7. ordena_intersecoes: tuplo → tuplo
ordena intersecoes(tup) recebe um tuplo de interseções (potencialmente vazio) e devolve um tuplo 
contendo as mesmas interseções ordenadas de acordo com a ordem de leitura do território.
'''

def ordena_intersecoes(tup):
    return tuple(sorted(tup, key=lambda x: (x[1], x[0]))) # Ordenar primeiro o número e depois letra


'''
2.1.8. territorio_para_str: territorio → cad. carateres
territorio para str(t) recebe um território e devolve a cadeia de caracteres que o representa 
(a representação externa ou representação “para os nossos olhos”), de acordo com o exemplo na 
seguinte interação.
'''

def territorio_para_str(t):
    # Verifica se o argumento é um território válido
    if not eh_territorio(t):
        raise ValueError("territorio_para_str: argumento invalido")

    linhas = [] # Uma lista vazia que vai ser preenchida
    Nv = len(t) # Número de caminhos verticais
    Nh = len(t[0]) # Número de caminhos horizontais

    # Adicione linha de letras
    linha_de_letras = ['  '] # Espaço para que a tabela esteja "direita"
    for v in range(Nv):
        linha_de_letras.append(chr(ord('A') + v)) # Converter em letras e adiciona-las na lista
    linhas.append(' '.join(linha_de_letras)) # Espaço entre letras

    for h in range(Nh - 1, -1, -1):
        linha = [str(h + 1).rjust(2)] # Adicionar os numeros no lado esquerdo(1a coluna)

        for v in range(Nv):
            if t[v][h] == 0:
                linha.append('.') # Se for 0 
            else:
                linha.append('X') # Se for 1

        linha.append(str(h + 1).rjust(2)) # Adicionar os números no lado direito(na última coluna)
        linhas.append(' '.join(linha))

    # Adicione letras de linha novamente (igual a primeira linha)
    linhas.append(' '.join(linha_de_letras))
    return '\n'.join(linhas) 


'''
2.2.1. obtem_cadeia: territorio × intersecao → tuplo
obtem cadeia(t,i) recebe um território e uma interseção do território (ocupada por uma montanha ou livre),
e devolve o tuplo formado por todas as interseções que estão conetadas a essa interseção ordenadas
(incluida si própria) de acordo com a ordem de leitura de um território.
'''

def obtem_cadeia(t, i):
    # Verificar se os argumentos são válidos (território e interseção)
    if not (eh_territorio(t) and eh_intersecao_valida(t, i)):
        raise ValueError("obtem_cadeia: argumentos invalidos")

    list_cadeia = [i] # Criar uma lista já com interseção i(inclui si própria)
    for cadeia in list_cadeia:
        if eh_intersecao_livre(t, cadeia): # Verifique se a interseção é livre 
            adjacentes = obtem_intersecoes_adjacentes(t, cadeia) # Obter interseções que rodeiam à volta da interseção
            for adjacente in adjacentes:
                if eh_intersecao_livre(t, adjacente) and not adjacente in list_cadeia: # Verifique se a interseção adjacente é livre
                    list_cadeia.append(adjacente) # Se fosse elegível adiciona na lista
        if not eh_intersecao_livre(t, cadeia): # Se a interseção é ocupada
            adjacentes = obtem_intersecoes_adjacentes(t, cadeia) # Obter interseções que rodeiam à volta da interseção
            for adjacente in adjacentes:
                if not eh_intersecao_livre(t, adjacente) and not adjacente in list_cadeia: # Verifique se a interseção adjacente é ocupada
                    list_cadeia.append(adjacente) # Se fosse elegível adiciona na lista
    return ordena_intersecoes(list_cadeia)

'''
2.2.2. obtem_vale: territorio × intersecao → tuplo
obtem vale(t,i) recebe um território e uma interseção do território ocupada por uma montanha, e devolve 
o tuplo (potencialmente vazio) formado por todas as interseções que formam parte do vale da montanha da 
interseçãao fornecida como argumento ordenadas de acordo à ordem de leitura de um território.
'''

def obtem_vale(t, i):
    # Verificar se os argumentos são válidos (território e interseções)
    # Verificar se a interseção é ocupada
    if not (eh_territorio(t) and eh_intersecao_valida(t, i)) or eh_intersecao_livre(t, i):
        raise ValueError("obtem_vale: argumentos invalidos")

    list_vale = [] # Uma lista vazia que vai ser preenchida
    cadeias = obtem_cadeia(t, i) # Conjunto de interseções
    for cadeia in cadeias:
        adjacentes = obtem_intersecoes_adjacentes(t, cadeia) # Obter adjacentes de cada interseção
        for adjacente in adjacentes:
            livre = eh_intersecao_livre(t, adjacente) # Vericar se o que está volta é livre
            if livre is True and not adjacente in list_vale: # Adiciona-se na lista se não está na lista
                list_vale.append(adjacente) 
    return ordena_intersecoes(list_vale) # Obter lista de vale com interseções ordenadas


'''
2.3.1. verifica_conexao: territorio × intersecao ×-intersecao → booleano 
verifica_conexao(t,i1,i2) recebe um território e duas interseções do território e devolve True se as duas interseçoes estão 
conetadas e False caso contrário.
'''

def verifica_conexao(t, i1, i2):
    # Verificar se os argumentos são válidos (território e interseções)
    if not (eh_territorio(t) and eh_intersecao_valida(t, i1) and eh_intersecao_valida(t, i2)):
        raise ValueError("verifica_conexao: argumentos invalidos")

    # Obter a lista de interseções que fazem parte da cadeia para a primeira interseção
    cadeia_i1 = obtem_cadeia(t, i1)

    # Verificar se a segunda interseção está na cadeia da primeira interseção
    return i2 in cadeia_i1


'''
2.3.2 calcula_numero_montanhas: territorio → int 
calcula_numero_montanhas(t) recebe um território e devolve o número de interseções ocupadas por montanhas no território.
'''

def calcula_numero_montanhas(t):
    # Verifica se o argumento é um território válido
    if not eh_territorio(t):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    
    soma = 0 
    Nv = len(t) # Número de caminhos verticais
    Nh = len(t[0]) # Número de caminhos horizontais

    for v in range(Nv):
        for h in range(Nh):
            if t[v][h] == 1: # Verifique se a interseção é ocupada(montanha)
                soma += 1
    return soma # Número de montanhas


'''
2.3.3. calcula_numero_cadeias_montanhas: territorio → int
calcula_numero_cadeias_montanhas(t) recebe um território e devolve o número de cadeias de montanhas 
contidas no território.
'''

def calcula_numero_cadeias_montanhas(t):
    # Verifica se o argumento é um território válido
    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")

    list_cadeia = [] # Uma lista vazia
    Nv = len(t) # Número de caminhos verticais
    Nh = len(t[0]) # Número de caminhos horizontais

    # Terminar todas as interseções ocupadas do território
    intersecoes = [] 
    for v in range(Nv):
        for h in range(Nh):
            if t[v][h] == 1: # Verifica se interseção é ocupada
                intersecao = chr(v + 65), h + 1 # Obtem interseção
                intersecoes.append(intersecao) # Conjunto de interseçõess ocupadas

    while intersecoes != []: # Um ciclo que só se acaba quando lista fica vazia
        for intersecao in intersecoes:
            cadeia = obtem_cadeia(t, intersecao) # Obter a cadeia

            # Remover as interseções(els) com cadeias já obtidas(para não repetir sempre a mesma coisa)
            for els in cadeia:
                if els in intersecoes:
                    intersecoes.remove(els) 

            if not cadeia in list_cadeia: 
                list_cadeia.append(cadeia)
    return len(list_cadeia) # Terminar o número de cadeias que existe no território


'''
2.3.4. calcula_tamanho_vales: territorio → int
calcula tamanho vales(t) recebe um território e devolve o número total de interseções 
diferentes que formam todos os vales do território.
'''

def calcula_tamanho_vales(t):
    # Verifica se o argumento é um território válido
    if not eh_territorio(t):
        raise ValueError ("calcula_tamanho_vales: argumento invalido")
    
    list_vale = [] # Lista vazia
    Nv = len(t) # Número de caminhos verticais
    Nh = len(t[0]) # Número de caminhos horizontais

    # Terminar todas as interseções ocupadas(montanha) do território
    intersecoes = [] 
    for v in range(Nv):
        for h in range(Nh):
            if t[v][h] == 1: # Verifique se a interseção é ocupada
                i = chr(v + 65), h + 1 # Converter em interseção
                intersecoes.append(i) 

    # Obter as vales
    for interct in intersecoes:
        adjacentes = obtem_intersecoes_adjacentes(t, interct) # Obter interseções adjacentes
        for adjacente in adjacentes:
            if eh_intersecao_livre(t, adjacente) and not adjacente in list_vale: # Verifica se é livre e não está na list_vale
                list_vale.append(adjacente) # Adiciona na lista se fosse elegível
    return len(list_vale) # Terminar o número de vales que existe no território
