"""

Programa Principal

"""

import random
import criptografia
import p0
import p1
import p2

numero_clientes = 10
clientes=[]

def cria_clientes():
    global clientes

    clientes = [None]*numero_clientes
    for i in range(0,numero_clientes):
        clientes[i]=[None]*numero_clientes

    for i in range(0,numero_clientes):
        for j in range(0,numero_clientes):
            clientes[i][j] = (None,[],[])

    return clientes

def le_palavras():
    arq=open("words.txt","r")
    return arq.readlines()

def main():
    # armazena tuplas (k,c,d) onde k:chave privada
    # d:mensagens decriptadas c: mensagens encriptadas 
    global clientes
    clientes=cria_clientes()
    words=le_palavras()

    i = random.randint(0,numero_clientes-1)
    j = random.randint(0,numero_clientes-1)

    usuario=clientes[i][j]
    y,c,d=usuario[0],usuario[1],usuario[2]
    if len(c)>0:
        for h in range(0,len(c)):
            key=y[h]
            d.append(criptografia.decripta(c[h],key))

    print("----------------------------")
    print("Mensagens entre cliente "+str(i)+" e "+"cliente "+str(j))
    print("----------------------------")
    for x in range(0,len(d)):
        print(d[x])
    print("----------------------------")
    r=random.randint(0,(len(words)-1))
    u=random.randint(0,(len(clientes)-1))
    print("cliente "+str(i)+" envia para cliente "+str(u)+" -> "+words[r])
    print("----------------------------\n\n\n")
    # envia para p0: msg, cliente que envia, cliente que recebe
    return words[r],i,u 
        
main()
    
