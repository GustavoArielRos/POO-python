from classes import Cliente
# Não é preciso importar essa classe , pois ela está dentro da classe Cliente
from classes import Endereco

cliente1 = Cliente('Luiz',32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente1.lista_enderecos()

cliente2 = Cliente('Maria',55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.lista_enderecos()

cliente3 = Cliente('João',19)
cliente3.insere_endereco('São Paulo', 'SP')
cliente3.lista_enderecos()

