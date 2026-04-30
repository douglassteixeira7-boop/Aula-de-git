#ATIVIDADE
#QUESTÃO 1
#Mostre números de 1 a 10, mas pare no 6.
# contador=1
# while contador<=10:
#     print(contador)
#     if contador==6:
#         break
#     contador+=1

    #QUESTÃO 2
#Mostre números de 1 a 10, pulando o número 5.
# numero=0
# while numero<10:
#     numero+=1
#     if numero==5:
#         continue
#     if numero==11:
#         break
#     print(numero)

   #QUESTÃO 3
#Mostre números de 1 a 20, pulando pares e encerrando no 15.

# contador=0
# while contador <20:
#     contador +=1
#     if contador %2==0:
#         continue
#     if contador==17:
#         break
#     print (contador)

#QUESTÃO 4
#Uma loja deseja cadastrar produtos até o funcionário digitar fim.

# while True:
#     produto=input("Digite o nome do produto:")
#     if produto=="fim":
#         print("Cadastro finalizado")
#         break
#     print("Produto Cadastrado", produto)

# Questão 5

# Parar quando soma chegar em 20
# soma=0
# while True:
#     numero= int(input("Digite um numero"))
#     soma+=numero
#     if soma >=20:
#         break
# print("Total",soma)

# ATIVIDADE

# Atividade 6 – Parada por Limite

# soma=0
# while True:
#     numero= int(input("Digite um numero"))
#     soma+=numero
#     if soma >=50:
#         print("Limite Atigindo!")
#         break
# print("Total",soma)

# Atividade 7 – Sistemas de Senha

# while True:
#     senha= input("Digite a senha:")
#     if senha== "teste":
#         print("Acesso Liberado")
#         break
#     else:
#         print("Senha incorreta")