pessoas = [];

nome1 = input('Digite seu nome: ')
idade1 = int(input('Digite sua idade: '))
cpf1 = int(input('Digite seu cpf: '))

pessoa1 = 'Nome: ' + nome1 + ' - ' + 'Idade: ' + str(idade1) + ' - ' + 'CPF: ' + str(cpf1)

pessoas.append(pessoa1)

print(pessoas[0])

