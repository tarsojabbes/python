capacidade_rev = float(input('Capacidade de revestimento? '))
print('')
print('== Dados do vão a revestir ==')
comprimento = float(input('Comprimento? '))
largura = float(input('Largura? '))
altura = float(input('Altura? '))
area = 2 * (largura * altura) + 2 * (comprimento * altura) + (comprimento * largura)
caixas = area / capacidade_rev
print('')
print('== Resultados ==')
print(f'Área total a revestir: {area:.1f} m2')
print(f'Número de caixas: {caixas:.0f}')
