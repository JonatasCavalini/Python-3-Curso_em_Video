
print('\033[31mTexto vermelho')
print('\033[31;43mTexto vermelho e fundo amarelo')
print('\033[1;31;43mTexto vermelho em negrito e fundo amarelo')
print('\033[1;31;43mTexto vermelho em negrito e fundo amarelo apenas até o final do texto\033[m')
print('\033[4;30;45mTexto branco sublinhado e fundo roxo apenas até o final do texto\033[m')
print('\033[7;30mTexto preto e fundo branco apenas até o final do texto\033[m')
print('\033[1;7;30mTexto preto em negrito e fundo branco apenas até o final do texto\033[m')

a = 3
b = 5
print('Os valores são \033[1;31m{} em vermelho e negrito\033[m e \033[1;33m{} em amarelo e negrito\033[m'.format(a, b))

nome = 'Guanabara'
print('Olá, {}{}{}!'.format('\033[1;31m', nome, '\033[m'))  # Variável "nome" em vermelho e negrito

cores = {
    'limpa': '\033[m',
    'azul': '033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m'
}

print('Olá, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))  # Variável "nome" em amarelo
