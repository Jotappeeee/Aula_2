# ### 5 -
#Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma
# palavra e concatene essa palavra no final da frase. Exiba o resultado.

frase = 'a vida é'
palavra = input('digite uma palavra: ')
print('ficou:', frase,palavra)


# # **6 -** 
# # **Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. 
# Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss".**

hours = int(input('digite a hora: '))
min = int(input('digite o minuto: '))
sec = int(input('digite o segundo: '))
print(f'Ficou: {hours}:{min}:{sec}')

# # **7 -
# Declare duas variáveis com números de telefone, incluindo um código de área e o número
# principal. Concatene esses valores para formar um número de telefone completo.**

ddd = int(input("Digite o DDD:"))
tel1 = int(input("Digite o numero de telefone:"))
print(f'Ficou: ({ddd}){tel1}')

# # **8 -
# # Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma 
# única string que liste os ingredientes separados por vírgulas.**

ing1 = 'polvilho doce'
ing2 = 'leite'
ing3 = 'ovos'
ing4 = 'oleo'
ing5 = 'sal'
ing6 = 'queijo'
print(f'Os ingredientes de um pão de queijo são: {ing1},{ing2},{ing3},{ing4},{ing5},{ing6}')

# # **9 -
# # Peça ao usuário para digitar três adjetivos e armazene-os em variáveis. Em seguida, 
# use essas palavras para criar uma frase concatenada que descreve algo interessante.**

adj1 = input('Digite um adjetivo: ')
adj2 = input('Digite mais um adjetivo: ')
adj3 = input('Digite mais um outro adjetivo: ')
print(f'A frase ficou assim: {adj1} {adj2} {adj3}')