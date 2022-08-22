
#A orientação a objeto clássica(de outras linguagens):

#    public -> métodos e atributos que podem ser acessados dentro e fora da classe
#    protect -> atributos que podem ser acessados apenas dentro da classe ou das filhas da classe
#    private -> atributo ou método só está disponível dentro da classe

#    Isso acima serve para proteger a sua aplicação



class BaseDeDados:
    def __init__(self):
        self._dados = {} # o underline indica que não é pra usar esse atributo fora da classe "1 underline"
        #self.__dados = {} #"2 underline" é um privado "mais forte" -> ele impede que esse atributo seja usado fora da classe

    def inserir_cliente(self,id,nome):
        # Para fazer um dicionário no qual cada key tenha um dicionario tambem
        if 'clientes' not in self._dados:
            self._dados['clientes'] = { id: nome}

        else:
            self._dados['clientes'].update({id : nome})

    # manipulando o dicionário( vai printar cada dado do dicionario)
    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self,id):
        del self._dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1,'Otávio')
bd.inserir_cliente(2,'Miranda')
bd.inserir_cliente(3,'Rose')

# o self.dados é um "public" é acessável por dentro e por fora
# acessando por fora eu posso "quebrar o esquema"
#bd.dados = 'Um outra coisa'


bd.lista_clientes()

