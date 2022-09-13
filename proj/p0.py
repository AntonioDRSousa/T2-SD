"""
modulo de rotinas do p0 no pipeline

"""

import criptografia
import script

# busca usuario a receber mensagem por nome num vetor com os usuarios
# retorna a posicao do elemento
def busca_usuario(us,usuarios):
    for i in range(0,len(usuarios)):
        if usuarios[i]==us:
            return i
    return -1
    
    

def processo_envio_p0(msg,us_in,us_out):
    # recebe de cliente: msg, cliente que envia, cliente que recebe
    pos = busca_usuario(us_out,script.clientes)
    if pos==(-1):
        print()# comando inutil
        # envia informacao de ausencia de usuario para o us_in
    else:
        key = criptografia.gera_chaves()
        priv_key = key[1]
        pub_key = key[0]
        
        # envia para cliente in e cliente out: priv_key
        envia_chave(us_in,us_out,priv_key)

        # envia para p1: pub_key, msg, pos
        

#envia chave privada para usuarios
def envia_chave(u1,u2,key):
    t=script.clientes[u1][u2]
    script.clientes[u1][u2]=(key,t[1],t[2])
    
    

