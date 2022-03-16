
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']  # Cria uma lista "lanche" com 4 itens (índices [0] a [3])
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']

lanche[3] = 'Picolé'  # Substitui o índice [3] ('Pudim') da lista "lanche" por 'Picolé'
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Pizza', 'Picolé'], com a lista já modificada pelo comando anterior

lanche.append('Cookie')  # Adiciona o item 'Cookie' ao final da lista "lanche", deixando-o na posição 5 (ou índice [4])
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Pizza', 'Picolé', 'Cookie'], com a lista novamente modificada
# Índices:                  [0]         [1]     [2]      [3]        [4]

lanche.insert(0, 'Cachorro Quente')  # Insere o item 'Cachorro Quente' no índice [0] da lista "lanche"
print(lanche)  # Exibe ['Cachorro Quente', 'Hambúrguer', 'Suco', 'Pizza', 'Picolé', 'Cookie']
# Índices:                     [0]             [1]         [2]     [3]      [4]        [5]

del lanche[3]  # Deleta o índice [3] ('Pizza') da lista "lanche"
print(lanche)  # Exibe ['Cachorro Quente', 'Hambúrguer', 'Suco', 'Picolé', 'Cookie']
# Índices:                     [0]             [1]         [2]     [3]        [4]

lanche.pop(0)  # Similar ao comando "del" anterior, deleta o índice [0] ('Cachorro Quente') da lista "lanche"
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Picolé', 'Cookie']
# Índices:                  [0]         [1]     [2]        [3]

lanche.pop()  # Usado sem especificar um valor entre parênteses, o método "pop()" deleta o último índice da lista ([3])
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Picolé']
# Índices:                  [0]         [1]     [2]

lanche.remove('Suco')  # Ao invés do índice, no método "remove()", deleta-se o item especificado entre parênteses
print(lanche)  # Exibe ['Hambúrguer', 'Picolé']
# Índices:                  [0]         [1]

if 'Pastel' in lanche:  # Se o item 'Pastel' estiver presente na lista "lanche"...
    lanche.remove('Pastel')  # Remove o item 'Pastel' da lista "lanche"
else:  # Senão...
    print("A lista não possui o item 'Pastel'.")  # Exibe uma mensagem
