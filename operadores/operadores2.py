# 2. Comparador de Áreas (Relacionais)
# Peça ao usuário as medidas de dois retângulos (Base e Altura para cada um). O programa deve imprimir True se a área do primeiro for maior que a do segundo, e False caso contrário.

# Operador sugerido: >.

base_retangulo1 = float(input('Base do Primeiro Retangulo: '))
base_retangulo2 = float(input('Base do Segundo Retangulo: '))

altura_retangulo1 = float(input('Altura do Primeiro Retangulo: '))
altura_retangulo2 = float(input('Altura do Segundo Retangulo: '))

area_retangulo1 = base_retangulo1 * altura_retangulo1
area_retangulo2 = base_retangulo2 * altura_retangulo2

if area_retangulo1 > area_retangulo2:
    print(True)
else:
    print(False)