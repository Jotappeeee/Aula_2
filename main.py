# 1 - Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?
age1= int(input('Digite a primeira idade: '))
age2= int(input('Digite a segunda idade: '))
if age1>age2 :
  print('A primeira idade é Maior que a segunda')
elif age1==age2 :
  print('As duas idades estão em igualdade')
else:
  print('A segunda idade é Maior que a primeira')
# 2 - Crie um sistema para permitir a verificação de menores em um show
age3= int(input('Digite a sua idade: '))
if age3>=18:
  print('Pode entrar no Show!!!')
else:
  print('Não pode entrar no show')
# 3 - Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de
#código if() para verificar se o aluno passou.
note1= float(input('Digite sua nota: '))
note2= float(input('Digite sua outra nota: '))
note3= float(input('Digite mais uma outra nota: '))
average= (note1+note2+note3)/3
if average>=7:
  print('Você passou')
else: 
  print('Você não passou')

