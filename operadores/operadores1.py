# 1. O Calculador de Descontos (Aritméticos)Crie um programa que receba o valor de um produto e o percentual de desconto. O script deve calcular o valor final.Dica: O cálculo segue a fórmula $ValorFinal = ValorOriginal \times (1 - \frac{Desconto}{100})$

valor_produto = int(input('Valor do Produto: '))
percentual_desconto = float(input('Desconto em %: '))

valor_final = valor_produto * (1 - (percentual_desconto / 100))

print(f'O valor final do produto é R$ {valor_final}')