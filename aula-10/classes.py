
# HERANÇA SIMPLES


# SUPER CLASSE(os métodos são globais)
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

        # Para saber qual classe está sendo executada(estou salvando no atributo o nome da classe)
        self.nomeclasse = self.__class__.__name__
    

    def falar(self):
        print(f'{self.nomeclasse}falando .....')


# SUB-CLASSES(tem métodos específicos)
# Herdando os atributos de outra classe
# Falando que cliente é uma pessoa
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse}comprando .....')
    
 

# Herdando os atributos de outra classe
# Falando que aluno é uma pessoa
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse}estudando .....')
    


