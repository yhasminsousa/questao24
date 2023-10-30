# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

nume = int(input("digite um número"))
for tabuad in range (10):
    result = tabuad * nume 
    print(f"{tabuad} * {nume} = {result}")