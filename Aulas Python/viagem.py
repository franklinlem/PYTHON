#posto = float(input('Estou no posto: '))
gas = float(input('O preço da gasolina é: R$ '))
alc = float(input('O preço do álcool é: R$ '))
if (alc/gas) <= 0.70:
    print("***ABASTEÇA COM ÁLCOOL!!!***")
else:
    print("***ABASTEÇA COM GASOLINA!!!***")
litros = float(input('Quantidade de combustível abastecido: '))
consumo = float(input('Qual a autonomia do veículo (km/L)?'))
auto = litros * consumo
print('Você poderá viajar por {} km com esse abastecimento.'.format(auto))
