num = int(input('Informe um número inteiro de três dígitos:'))

if 100 <= num <= 999:
    num = str(num)
    print(f'O número em ordem invertida é {num[::-1]}.')
else:
    print(f'O número informado não possui três dígitos,'
          f'tente novamente inserindo um número de três dígitos.')
