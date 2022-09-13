"""

Programa Principal

"""

import random
import criptografia
import p0
import p1
import p2

numero_clientes = 10

def cria_clientes():
    clientes = [None]*numero_clientes
    for i in range(0,numero_clientes):
        clientes[i]=[None]*numero_clientes
    for i in range(0,numero_clientes):
        for j in range(0,numero_clientes):
            clientes[i][j] = ("cliente "+str(i),None,[],[])
    return clientes

def le_palavras():
    arq=open("words.txt","r")
    words=arq.readlines()
    return words

def main():
    # armazena tuplas (x,y,c,d) onde x : nome e y:chave privada
    # d:mensagens decriptadas c: mensagens encriptadas 
    clientes=cria_clientes()
    print(clientes)
    words=le_palavras()
    print(words[0:9])
    for i in range(0,numero_clientes):
        for j in range(0,numero_clientes):
            usuario=clientes[i][j]
            key=usuario[1]
            c=usuario[2]
            d=usuario[3]
            if len(c)>0:
                for j in range(0,len(c)):
                    decrypt = criptografia.decripta(c[j],key)
                    d.append(decrypt)
        print("----------------------------")
        print("cliente "+str(i))
        print("----------------------------")
        for i in range(0,len(d)):
            print(d[i])
        print("----------------------------")
        r=random.randint(0,(len(words)-1))
        print("envia -> "+words[r])
        print("----------------------------\n\n\n")
        
        

main()
    
