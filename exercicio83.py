expressao = input("Digite uma expressão: ")

pilha = []

for simbolo in expressao:
    if simbolo == "(":
        pilha.append(simbolo)

    elif simbolo == ")":
        if len(pilha) == 0:
            print("Expressão inválida!")
            break
        pilha.pop()
else:
    if len(pilha) == 0:
        print("Expressão válida!")
    else:
        print("Expressão inválida!")
