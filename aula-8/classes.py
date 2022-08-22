# AGREGAÇÃO


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos =[]

    def inserir_produto(self,produto):
        self.produtos.append(produto)
    
    # nessas 2 funções eu "uso" os atributos da outra classe "produto.nome" e "produto.valor"
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor

        return total


class Produto:
    def __init__(self,nome,valor):
        # Os atributos que serão usados na outra classe
        self.nome = nome
        self.valor = valor

