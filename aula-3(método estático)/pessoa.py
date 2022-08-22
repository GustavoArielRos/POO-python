# METODOS ESTÁTICO

from random import randint

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
        print(idade)
        #return cls(nome, idade)

    @staticmethod # ele não recebe classe ou instancia(ele PODE receber parametros)
    def gera_id():
        # pode se criar variaveis sem "self" ou "cls"
        rand = randint(10000, 19999)
        return rand

    #Se o método tem haver(específico) com a classe -> cls
    #Se o método tem haver(específico) com a instância -> self
    #Se o método tem haver(específico) com uma "função normal" -> sem self e cls
    
