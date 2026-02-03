# 3. Validador de Senha (while)
# Crie um programa que peça uma senha ao usuário. Enquanto a senha digitada for diferente de "python123", o programa deve exibir "Acesso Negado. Tente novamente" e pedir a senha outra vez. Quando ele acertar, exiba "Acesso Liberado!".

while True:
    senha = str(input('Senha de usuario: '))
    if senha == 'python123':
        break
print('login aceito')