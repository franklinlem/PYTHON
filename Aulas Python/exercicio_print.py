## pintar uma parede de a metros quadrados usando b litros de tinta.
## cada 18 litros pinta 30 metros de parede
## uma lata de 18 litros custa 180 reais.
##Qto vai gastar para pintar uma casa com 180 m² de parede?

area = float(input('Qual a área a ser píntada? '))
tinta = area * (18/30)
custo = tinta * (180/18)
latas = tinta / 18
print('Para pintar uma área de {:.2f} m²:'.format(area))
print('Serão necessários {:.2f} litros de tinta.'.format(tinta))
print('O custo da tinta será de R$ {:.2f}.'.format(custo))
print('Vai precisar de {:.2f} latas.'.format(latas))
