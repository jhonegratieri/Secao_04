"""
Como os dados do problema traz duas variiáveis, comprimento e largura,
e não me informou qual o formato do terreno, vou considerar que se trata
de um terreno retangular, no qual pretende-se cercar os quatro lados.
"""
l = float(input("Informe a largura do terreno em metros:"))
c = float(input("Informe o comprimento do terreno em metros"))
valor = float(input('Informe o valor por metro da tela a ser utilizada em reais:'))
valortotal = 2 * (l + c) * valor
print(f"\nO custo para cercar esse terreno é de {valortotal} reais.")
