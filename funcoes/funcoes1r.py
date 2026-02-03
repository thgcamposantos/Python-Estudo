receitas = 3500
gastos = [500, 300, 450, 600, 250]

def f_calcular_saldo(ff_receitas , ff_gastos):
    f_total_gastos = sum(ff_gastos)
    saldo = ff_receitas - f_total_gastos
    return saldo

def f_classifica_saldo(f_saldo):
    if f_saldo == 0:
        return 'Zerado'
    else:
        return 'Positivo'
    
def f_total_gastos(f_gastos):
    return sum(f_gastos)
        
def relatorio(f_receitas , f_gastos):
    calculo = f_calcular_saldo(f_receitas , f_gastos)
    print(calculo)
    classificacao = f_classifica_saldo(calculo)
    print(classificacao)
    total_gastos = f_total_gastos(gastos)
    print(total_gastos)


relatorio(receitas , gastos)
