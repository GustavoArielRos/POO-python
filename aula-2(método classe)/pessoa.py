
# METODOS DE CLASSES
class Pessoa:
    ano_atual = 2019

    def __init__(self, nome ,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    #criando método de classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento): #cls -> serve para se referir a classe e não a instancia(no caso o 'self' se refere a instancia), com isso você tem acesso a variavel global da classe "ano_atual"
        # usando o cls para se referir a variavel da classe
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)