# 3. Sistema de Venda de Ingressos (Lógicos)
# Para entrar em um clube, o cliente precisa:

# Ter mais de 18 anos.

# OU estar acompanhado dos pais.

# E ter o ingresso pago.

# Crie variáveis booleanas para essas condições e use os operadores and, or e not para verificar se a entrada é permitida.

idade = int(input('Idade: '))
pagamento = True

if idade < 18 and pagamento == True:
    responsavel = str(input('Está com responsavel (Responda sim ou não): ')).lower()
    if responsavel[0] == 's':
        print('Acesso permitido')
    else:
        print('Acesso negado')
elif idade >= 18 and pagamento == True:
    print('Acesso permitido')
else:
    print('Acesso negado')
