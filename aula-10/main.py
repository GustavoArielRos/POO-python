
from classes import*

c1 = Cliente("Luiz", 45)
a1 = Aluno('Maria',54)

# o método "falar" pode ser usado nas duas classes ( Cliente e Aluno)
# Porém cada uma dessas classes possuem métodos específicos que só podem ser usados nelas mesmo
c1.falar()
c1.comprar()

a1.falar()
a1.estudar()

# Se eu usar a instância com a classe "Pessoa"("Classe mãe") eu só vou ter o método "falar()"

p1 = Pessoa("Carlos",22)
p1.falar()

