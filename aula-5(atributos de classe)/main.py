# ATRIBUTO DE CLASSE

# atributo = variável da classe

class A:
    vc = 123


a1 = A()
a2 = A()

# imprimindo a variavel da classe usando a instancia
print(a1.vc)
print(a2.vc)   

# imprimindo a variavel da classe usando o nome da classe
print(A.vc)

# mudando o valor da variavel da classe pelo nome da classe
A.vc = 321

# mudando o valor da variavel usando uma instancia

a1.vc = 432 # porem voce só muda o valor da variavel nessa instancia "a1" na "a2" o valor da variavel é o padrao

