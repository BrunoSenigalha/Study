nome_sobrenome = 'Bruno Senigalha' #str
idade = 14 #int
maior_de_idade = idade >= 18 

print(nome_sobrenome)

while idade <= 18 :
    contador_idade = 18 - idade
    maior_de_idade = idade >= 18 

    if maior_de_idade == True:
        print('Maior de idade'),
        print(f'{idade} anos')
        print('Parabéns, você resolveu um problema de lógica simples')
        print()

    
    else:
        print('Menor de Idade'),
        print(f'{idade} anos'),
        print("Faltam", contador_idade, "anos para completar 18 anos")
        print()
        print()
    
    idade = idade + 1
        
    

   
    
