# input recebe dados digitados pelo usuário
# input sempre receberá string quando for digitado
# depois é necessário fazer a conversão para o tipo de variável desejável

numero_1 = input('Digite um número: ') 
numero_2 = input('Digite outro número: ')

if numero_1.isdigit() and numero_2.isdigit(): # O método isdigit verifica se o usuário digitou um número
    int_numero_1 = int(numero_1)
    int_numero_2 = int(numero_2)
    print(f'A soma dos números é {int_numero_1 + int_numero_2}')
    
else:
    print("É para digitar números caralho!")

# if numero_1.isalpha() or numero_2.isalpha(): # O método isdigit verifica se o usuário digitou uma letra

#     print('DIGITA SÓ NÚMEROS SATANAAAAAAAAAS!')

# else:
#     int_numero_1 = int(numero_1)
#     int_numero_2 = int(numero_2)
#     print(f'A soma dos números é {int_numero_1 + int_numero_2}')


    

