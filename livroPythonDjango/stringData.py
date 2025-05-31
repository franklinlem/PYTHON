#Convertendo strings em datas
from datetime import datetime
data_string = input('Entre uma data no formato mm/dd/yyyy: ')
print('Você forneceu: ', data_string)

uma_data = datetime.strptime(data_string, '%d/%m/%Y')

print('Após a conversão, a data fornecida contem:')
print(f'Dia: {uma_data.day}')
print(f'Mês: {uma_data.month}')
print(f'Ano: {uma_data.year}')

str_nascimento = input('Digite sua data de nascimento no formato dd/mm/yyyy: ')
data_nasc = datetime.strptime(str_nascimento, '%d/%m/%Y')
idade = datetime.now() - data_nasc

print(f'Você tem {idade.days} dias de vida.')