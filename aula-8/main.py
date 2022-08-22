from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta',50)
p2 = Produto('Iphone',10000)
p3 = Produto('Caneca', 15)

# assim não aparece nada
carrinho.lista_produto()

# agora eu estou adicionando
carrinho.lista._produto(p1)
carrinho.lista._produto(p2)
carrinho.lista._produto(p3)