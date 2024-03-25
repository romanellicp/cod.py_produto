import moeda

p = float(input('Digite o preço do produto: R$ '))
print(f'A metade do preço do produto é {moeda.metade(p)} R$')
print(f'O dobro do preço do produto é {moeda.dobro(p)} R$')
print(f'O produto com 10% de taxa fica {moeda.aumento(p, 10)} R$')
print(f'O produto com 10% de desconto fica {moeda.diminuir(p, 10)} R$')