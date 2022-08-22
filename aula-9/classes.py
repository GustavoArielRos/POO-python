# COMPOSIÇÃO
# Usasse os atributos de uma classe em outra classe
# UMA CLASSE PERTENCE A OUTRA CLASSE
# A classe "Endereço" pertence a classe "Cliente"

class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    # usando a classe "Endereco" nesse método(função)
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade , estado))
    
    # usando os atributos da classe "Endereco" nesse método(função)
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado
