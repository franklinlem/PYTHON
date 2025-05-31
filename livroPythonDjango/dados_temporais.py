#Calculando diferença entre datas e horas (objeto timedelta)
#delta = datetime.timedelta(dias, segundos, microssegundos, milisegundos, minutos, horas, semanas)
import datetime
from datetime import timedelta

d = timedelta(days=365, hours=8, minutes=15)
agora = datetime.datetime.now()

print(f'Em 365 dias, 8 horas e 15 minutos, será {agora+d}')