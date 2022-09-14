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
    
    qtd= int(input("Quantas voltas do script de comunicacao aleatoria?"))
    for k in range(0,qtd):
        for i in range(0,numero_clientes):
            for j in range(0,numero_clientes):
                usuario=clientes[i][j]
                y,c,d=usuario[0],usuario[1],usuario[2]
                if len(c)>0:
                    for j in range(0,len(c)):
                        key=y[j]
                        d.append(criptografia.decripta(c[j],))

            print("----------------------------")
            print("Mensagens entre cliente "+str(i)+" e "+"cliente "+str(j))
            print("----------------------------")
            for i in range(0,len(d)):
                print(d[i])
            print("----------------------------")
            r=random.randint(0,(len(words)-1))
            u=random.randint(0,(len(clientes)-1))
            print("cliente "+str(i)+" envia para cliente "+str(u)+" -> "+words[r])
            r=random.randint(0,(len(words)-1))
            u=random.randint(0,(len(clientes)-1))
            print("cliente "+str(j)+" envia para cliente "+str(u)+" -> "+words[r])
            print("----------------------------\n\n\n")
        
main()
    
