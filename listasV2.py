import time, sys, os
count = 0
vezes = 0
achados = 0
achou = []
notificar = []
lista = []

print('-' * 40)
print(f'{"Bem-Vindo!":^40}')
print('-' * 40)

while True:

	print('\n')
	auto = str(input('Digite o número do auto.\n '))
	vezes += 1
	notificar.append(auto)

	if auto in lista:
		print('\n')
		print('Consta na Lista')
		print(f'O auto é o número {lista.index(auto)} na sequência')
		count += 1
		achados += 1
		achou.append(auto)

		if vezes == 5:
			vezes -= 5
			print('\n')
			print('Aguarde...')
			for i in range(0, 2):
					sys.stdout.flush()
					time.sleep(1)
			os.system('cls')
			print(f'Você parou no {auto}, continue.')

		if count == 5:
			count -= 5
			print(f'Parabéns, você já encontrou {achados} autos!')
			print('\n')
			continuar = str(input('Deseja continuar procurando? [S/N] ')[0].upper().strip())

			if continuar == 'N':
				print('-' * 40)
				print(f'Você achou os seguintes autos...\n {achou}\n')
				print(f'Você achou', len(achou), 'autos\n')

				print(f'Você procurou os seguintes autos...\n {notificar}\n')
				print(f'Você pesquisou', len(notificar), 'autos')
				print('-' * 40)
				print('Até logo!')
				fechar = str(input('Fechar Programa? [S/N] ')[0].upper().strip())
				if fechar == 'S':
					print('Fechando Programa...')
					print('-' * 40)
					for i in range(0, 3):
						sys.stdout.flush()
						time.sleep(1)
					break

	else:
		print('\n')
		print('Não consta na Lista.')
		

		if vezes == 5:
			vezes -= 5
			print('\n')
			print('Aguarde...')
			for i in range(0, 2):
					sys.stdout.flush()
					time.sleep(1)
			os.system('cls')
			print(f'Você parou no {auto}, continue.')
