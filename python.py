# Tuplas podem guardar várias informações e são formadas com "()"
Tupla = ('item1, item2, item3, item4')

# Tuplas são imutáveis!
# Mas podemos buscar por informações das tuplas como feito a seguir:

#index() - Busca pela posição no index do item especificado dentro do "()"
frutas = ('maçã', 'banana', 'pera', 'maracujá', 'uva')
indice_pera = frutas.index('pera')
print(f"O índice do item procurado é {indice_pera}")
#Resultado: O índice do item procurado é 2

#count() - Busca pela quantidade do item especificado dentro do "()" na tupla
cores = ('rosa', 'preto', 'rosa', 'rosa', 'amarelo', 'laranja', 'vermelho')
quantidade_rosa = cores.count('rosa')
print(f"A quantidade de cores rosa na tupla é {quantidade_rosa}")
#Resultado: A quantidade de cores rosa na tupla é 3

#len() - Mostra o tamanho da tupla
nomes = ('Felipe', 'Júlia', 'Eduardo', 'Carlos')
Tamanho_nomes = len(nomes)
print(f'A tupla possui {Tamanho_nomes} pessoas')
#Resultado: A tupla possui 4 pessoas
