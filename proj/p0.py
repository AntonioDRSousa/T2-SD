"""
modulo de rotinas do p0 no pipeline

"""

import criptografia
import script   

def processo_envio_p0(msg,us_in,us_out):
    # recebe de cliente: msg, cliente que envia, cliente que recebe
    
    if us_out>=script.numero_clientes:
        # envia informacao de ausencia de usuario para o us_in
        print("\n\n\n----------------------------")
        print("cliente "+str(us_in))
        print("!!! Usuario cliente "+str(us_out)+" Inexistente !!!")
        print("----------------------------\n\n\n")
    else:
        key = criptografia.gera_chaves()
        priv_key = key[1]
        pub_key = key[0]
        
        # envia para cliente in e cliente out: priv_key
        envia_chave(us_in,us_out,priv_key)

        # envia para p1: pub_key, priv_key msg, us_in, us_out
        return pub_key, priv_key, msg, us_in, us_out
        

#envia chave privada para usuarios
def envia_chave(u1,u2,key):
    t=script.clientes[u1][u2]
    script.clientes[u1][u2]=((t[0]).append(key),t[1],t[2])
    
    

