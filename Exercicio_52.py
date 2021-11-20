a1 = float(input("Informe quantos reais o primeiro amigo contribuiu para a aposta:"))
a2 = float(input("Informe quantos reais o segundo amigo contribuiu para a aposta:"))
a3 = float(input("Informe quantos reais o terceiro amigo contribuiu para a aposta:"))
p = float(input("Informe o valor total do prêmio:"))

p1 = (a1 / (a1 + a2 + a3)) * p
p2 = (a2 / (a1 + a2 + a3)) * p
p3 = (a3 / (a1 + a2 + a3)) * p

print(f"\nO primeiro amigo ganhou {p1} reais do prêmio")
print(f"O segundo amigo ganhou {p2} reais do prêmio")
print(f"O terceiro amigo ganhou {p3} reais do prêmio")
