# 1. Simulador de Semáforo (if, elif, else)
# Crie um programa que receba a cor de um semáforo (Verde, Amarelo ou Vermelho).

# Se for Verde, exiba "Siga".

# Se for Amarelo, exiba "Atenção".

# Se for Vermelho, exiba "Pare".

# # Se for qualquer outra coisa, exiba "Cor inválida".

semaforo = str(input('Cor do semaforo: ')).lower()
if semaforo == 'verde':
    print('Siga')
elif semaforo == 'amarelo':
    print('Siga com atenção')
else:
    print('Pare')