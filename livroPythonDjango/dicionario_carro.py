print('\nCriando um dicionário para armazenar os dados de um carro...')
carro={
    'marca':'Hyundai',
    'modelo':'HB20',
    'ano': 2015,
    'motorização': 1.6,
    'cambio':'automático',
    'acessórios':[],
}
print('\nDicionario criado!\n', carro)

carro['ano']=2018
carro['modelo']='HB20 R-Spec'
print('\nTroquei de carro... comprei um mais novo!', carro)

print('\nColocando acessorios no carro: ')
carro['acessórios']=['alarme']
print('\nInstalei um alarme novo: \n', carro)

carro['acessórios'].append('som')
print('\nColoquei um novo som: \n', carro)

carro['acessórios'][1]='som diferente'
print('\nTroquei o modelo do som: \n', carro)

#apagar um item de dicionário:
del carro['acessórios']
print("\nApaguei os acessórios.\n", carro)