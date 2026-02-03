# 4. Filtro de Lista (for e if)
# Dada a lista de números notas = [8.5, 4.0, 7.5, 3.0, 10, 5.5], percorra a lista e, para cada nota:

# Se a nota for maior ou igual a 7, imprima "Aprovado".

# Caso contrário, imprima "Reprovado".
notas = [8.5, 4.0, 7.5, 3.0, 10, 5.5]

for n in notas:
    if n >= 7:
        print(f'A nota é: {n} e o aluno está aprovado')
    else:
        print(f'A nota é: {n} e o aluno está reprovado')