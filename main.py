hero = ("pedro", 10, 100, 1500)
nome, nivel, vida, exp = hero
print("O herói " + nome + " está no nível " + str(nivel) + "com " + str(vida) + " HP e "+ str(exp) + " XP")



spawn_point = (0, 0, 0)
x ,y, z = spawn_point
print("X: "+ str(spawn_point[0]) +"\nY: "+ str(spawn_point[1]) +"\nZ: "+ str(spawn_point[2]))


moedas = (5, 10, 2)
valores = (5, 3, 1)

ouro, bronze, prata = moedas
valor_ouro, valor_bronze, valor_prata = valores

print("moedas de cada tipo:")
print("ouro: " + str(ouro) +", bronze:" + str(bronze) +", prata: " +str(prata))

total = ouro+bronze+prata
print("total de moedas:" + str(total))

valor_moeda_ouro = ouro * valor_ouro
valor_moeda_bronze = bronze * valor_bronze
valor_moeda_prata = prata * valor_prata
print("valor de ouro: " + str(valor_moeda_ouro) + "valor da prata: " + str(valor_moeda_prata) +" valor do bronze: " + str(valor_moeda_bronze))
valores = valor_moeda_ouro + valor_moeda_bronze + valor_moeda_prata
print("valor total: " + str(valores))


scores = ("Ana", "Bruno", "Carla", "David", "Eva")
primeiros = scores[:2]
outros = scores[2:]

print(primeiros)
print(outros)

