"""

Programa Principal

"""

import random
import criptografia
import p0
import p1
import p2

import xmlrpc.client

from clientes import clientes, numero_clientes

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

def le_palavras():
    arq = open("words.txt","r")
    return arq.readlines()

def main():
    words = le_palavras()

    i = random.randint(0, numero_clientes - 1)
    j = random.randint(0, numero_clientes - 1)

    y, c, d = clientes[i][j]
    
    if len(c) > 0:
        for h in range(len(c)):
            d.append(criptografia.decripta(c[h], y[h]))

    print("----------------------------")
    print("Mensagens entre cliente", str(i), "e cliente", str(j))
    print("----------------------------")
    
    for x in d:
        print(x)
        
    print("----------------------------")
    
    r = random.randint(0, len(words) - 1)
    u = random.randint(0, len(clientes) - 1)
    
    print("cliente", str(i), "envia para cliente", str(j), "->", words[r])
    print("----------------------------\n\n\n")

    # envia para p0: msg, cliente que envia, cliente que recebe
    response = proxy.service((words[r], i, j))
    print(response)

main()
    
