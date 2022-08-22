# ASSOCIAÇÃO

# classe se relaciona com classe , porém uma NÃO precisa da outra para "viver"

from classes import Escritor, MaquinaDeEscrever
from classes import Caneta

escritor = Escritor('Joãozinho')
print(escritor.nome)

caneta = Caneta('Bic')
print(caneta.marca)

maquina = MaquinaDeEscrever()

# Usando a classe Escritor e a classe Caneta

escritor.ferramenta = caneta #"ferramente" é da classe Escritor # Eu no caso estou enviando a classe "Caneta" inteira para o objeto "ferramenta"(que é um atributo da classe "Escritor"), pois caneta= Caneta() -> eu coloquei isso antes
escritor.ferramenta.escrever() # "escrever() é um método da classe "Caneta"
