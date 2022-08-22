# Getters e Setters
# Serve para "consertar os problemas"
# Você utiliza-os em cada atributo 

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual /100))

       
    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        # chegando se o valor é uma instância do tipo string
        if isinstance(valor, str):
            valor = float(valor.replace('R$', '')) # o replace eu tirei o 'R$'  e coloquei nada
        self._preco = valor

    # Fazendo isso para o atributo 'nome'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def preco(self, valor):
        # Colocando para só a primeira letra ser maiuscula
        self._nome = valor.title()

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

# Aqui da erro , pois o parâmetro que era para ser int virou uma string
p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco) 

p3 = Produto('CANECA', 'R$15')
p3.desconto(10)
print(p3.preco)