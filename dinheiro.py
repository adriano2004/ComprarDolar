d = float(input('Quantos reais você tem na carteira? '))
dolar = 5.56 #Cotação do dia que foi criado o código
valor=(d/dolar) #Faz calculo de quantos dolares é possivel comprar com o dinheiro na carteira

print('Você pode comprar US$ {:.2f} dolares com R$ {} '.format(valor,d))