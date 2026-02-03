# 5. Conversor de Dias (Divisão Inteira e Resto)
# Peça ao usuário um número total de dias e converta para o formato: X semanas e Y dias.

# Exemplo: 15 dias = 2 semanas e 1 dia.

# Operadores sugeridos: // (divisão inteira) e % (resto).

total_dias = int(input('Total de dias: '))
if total_dias / 7 < 0:
    dias = total_dias
    print(f'total de dias é: {dias}')
elif total_dias == 7:
    dias = total_dias
    print(f'Total dias é: {dias}')
else:
    semana = int(total_dias / 7)
    dias = int(total_dias % 7)
    print(f'Total semanas é: {semana} e de dias é: {dias}')