"""
a1 = int(input("Digite o primeiro valor de A: "))
a2 = int(input("Digite o segundo valor de A: "))


b1 = int(input("Digite o primeiro valor de B: "))
b2 = int(input("Digite o segundo valor de B: "))

"""

import funcoes

a = [1, 4, 2, 3, 4, 2, 3]


print(f"a original       {a}")
sem_repeticao = funcoes.distintos(a)
print(f"a sem repetições {sem_repeticao}")


