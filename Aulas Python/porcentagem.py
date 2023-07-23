preço = float(input('O preço da mercadoria é R$ '))
desc = float(input('O desconto(%) será de '))
eco = preço * desc/100
novo = preço - eco

print('Com desconto de {:.1f} % você irá pagar R$ {:.2f} pelo produto.'.format(desc, novo))
print("Parabéns!!! Você economizou R$ {:.2f}! \n     Que fofinho!!!".format(eco))
