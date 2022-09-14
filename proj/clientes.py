numero_clientes = 100


# para clientes i e j armazena tuplas (k,c,d) onde:
# k: chave privada
# d: mensagens decriptadas
# c: mensagens encriptadas

clientes = [[([], [], []) for i in range(numero_clientes)] for j in range(numero_clientes)]
