# 2. A Tabuada Automática (for)
# Peça ao usuário um número inteiro e, utilizando um laço for, imprima a tabuada desse número de 1 a 10.

# Dica: Use a função range(1, 11).

numero = int(input('Numero: '))
for n in range(1,11):
    print(f'{numero} x {n} = {numero * n}')
