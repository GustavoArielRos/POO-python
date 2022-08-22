from pessoa import Pessoa

# chamando o método estático pela classe
print(Pessoa.gera_id())

# chamando o método estático pela instância
p1 = Pessoa('Luiz',32)
print(p1.gera_id())