num = int(input('Informe um número inteiro de quatro dígitos:'))

if 1000 <= num <= 9999:
    num = str(num)
    print(f'{num[0]}\n{num[1]}\n{num[2]}\n{num[3]}')

else:
    print(f'O número informado não possui quatro dígitos,'
          f'tente novamente inserindo um número de quatro dígitos.')
