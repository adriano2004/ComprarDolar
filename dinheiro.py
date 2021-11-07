d = float(input('Quantos reais você tem na carteira? R$'))
dolar = d/5.56 #Cotação do dia que foi criado o código
euro = d/6
pm = d*3.67
print('Você pode comprar com R$ {} '.format(d))
print('US$ {:.2f} \n€ {:.2f} \nMX$ {:.2f}'.format(dolar,euro,pm))