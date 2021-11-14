import math
#Resolução da questão #20 do projecteuler.net por Saulo Freitas

listaFat = list(str(math.factorial(100))) # cria-se lista contendo fatorial, é convertida para string para permitir iteração

listaFatInt = [int(i) for i in listaFat] # novo array realizando a conversão dos valores para int, possibilitando o cálculo necessário

somaFatorial = sum(listaFatInt) #soma dos componentes que integram a lista

print('resultado: ',somaFatorial) # saida do resultado