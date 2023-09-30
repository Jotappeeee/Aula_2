# numero = int(input('digite algo:' ))

# if numero > 8:
#   print ("okay")
# else:
#   print ('nao')

# name = str(input('Digite seu nome: '))
# age = int(input('Digite sua idade: '))
# shopping = float(input('Digite suas compras do mês: '))
# shopping2 = float(input('Digite suas compras do mês anterior: '))

# print('\nNome: ', name, '\nIdade: ', age, '\nSoma das compras:',shopping + shopping2)
# print('   ')

# name1 = str(input('Digite seu nome: '))
# age1  = int(input('Digite sua idade: '))
# my_address = input('Digite seu endereço: ')
# office = input('Digite seu cargo: ')

# print('Meu nome é', name1, 'minha idade é', age1, 'meu endereço é', my_address,'Meu cargo é', office) 
# print(f'Meu nome é {name1}, minha idade é {age1}, meu endereço é {my_address}, Meu cargo é {office}') 

# #---------------------------------------------------------------------------------------

# num = float(input('Digite algo: '))

# if num == 10:
#   print(f'O numero é {num} ;)')
# else:
#   print(f'O numero é {num} :(')


password = int(input('Digite algo: '))
password_true = 1234
name = input('Digite algo: ')
name_true = "jota" 
           
if password == password_true and name == name_true:
  print('Acesso Permitido!')
elif password != password_true and name == name_true:
  print('Senha errada!')
elif password == password_true and name != name_true:
  print('Nome errada!')
else:
  print('tudo errado')

