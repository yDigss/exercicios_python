from random import randint

numeros = (randint(1 , 10), randint(1 , 10), randint(1 , 10), randint(1 , 10), randint(1 , 10))
print("Os valores sorteados foram: ")

for n in numeros:
    print(f"{n} ", end=" ")
print(f"\nO maior valor sorteador foi {max(numeros)}")
print(f"O menor valor sorteador foi {min(numeros)}")