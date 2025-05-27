import datetime
from pickletools import anyobject
import time

hoje = datetime.date.today()

print('Hoje é dia ', hoje)

print('Hoje é dia: ', hoje.strftime("%d/%m/%Y"))

print('Hoje é: ', hoje.strftime("%A"))

print('Estamos no mês de: ', hoje.strftime("%B"))

print('\nTempo em segundos desde a data base 01/01/1970 - 12:00am: \n', time.time())

print('\nTodos os atributos da tupla time: \n', time.localtime(time.time()))

print('\nData e hora atual: ', time.time())

print('\nTupla time contendo elementos de data e hora atual.\n', time.localtime())

#incializando uma variávl com umvalor do tipo datetime
#variavel = datetime.datetime(ano, mês, dia, hora, minuto, segundo, microssegundo, timezone, fold)

uma_data=datetime.datetime(2025, month=5, day=27)

print('\nVariavel = ', uma_data)

#representando horas com time
#variavel = datetime.time(15, 57, 1)

hora = datetime.time(15, 57, 1)

print('\nHora: ', hora)