a = float(input('Informe a altura do degrau:'))
at = float(input('Informe a altura total que deseja atingir:'))
div = int(at/a)

if at % a > 0:
    print(f'Você precisrá subir {div + 1} degraus para alcançar a altura desejada.')
else:
    print(f'Você precisrá subir {div} degraus para alcançar a altura desejada.')
